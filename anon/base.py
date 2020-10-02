# stdlib
from collections import OrderedDict
from logging import getLogger

# deps
from chunkator import chunkator_page

# local
from anon.compat import bulk_update


logger = getLogger(__name__)


class OrderedDeclaration(object):
    """ Any classes inheriting from this will have an unique global counter
        associated with it. This counter is used to determine the order in
        which fields were declarated

        Idea taken from: https://stackoverflow.com/a/4460034/639465
        Also inspired by https://github.com/FactoryBoy/factory_boy
    """

    global_counter = 0

    def __init__(self):
        self._order = self.__class__.global_counter
        self.__class__.global_counter += 1


class LazyAttribute(OrderedDeclaration):
    def __init__(self, lazy_fn):
        super(LazyAttribute, self).__init__()
        self.lazy_fn = lazy_fn

    def __call__(self, *args, **kwargs):
        return self.lazy_fn(*args, **kwargs)


def lazy_attribute(lazy_fn):
    """ Returns LazyAttribute objects, that basically marks functions that
        should take `obj` as first parameter. This is useful when you need
        to take in consideration other values of `obj`

        Example:

        >>> full_name = lazy_attribute(o: o.first_name + o.last_name)

    """
    return LazyAttribute(lazy_fn)


class BaseAnonymizer(object):
    def run(self, select_chunk_size=None, **bulk_update_kwargs):
        self._declarations = self.get_declarations()

        queryset = self.get_queryset()
        update_fields = list(self._declarations.keys())
        update_batch_size = bulk_update_kwargs.pop(
            "batch_size", self._meta.update_batch_size
        )

        if select_chunk_size is None:
            select_chunk_size = self._meta.select_chunk_size

        if update_batch_size > select_chunk_size:
            raise ValueError(
                "update_batch_size ({}) should not be higher than "
                "select_chunk_size ({})".format(update_batch_size, select_chunk_size)
            )

        # info used in log messages
        model_name = self._meta.model.__name__
        current_batch = 0

        for page in chunkator_page(queryset, chunk_size=select_chunk_size):
            logger.info(
                "Updating {}... {}-{}".format(
                    model_name, current_batch, current_batch + select_chunk_size
                )
            )
            current_batch += select_chunk_size

            objs = []
            for obj in page:
                self.patch_object(obj)
                objs.append(obj)

            bulk_update(
                objs,
                self.get_manager(),
                **dict(
                    update_fields=update_fields,
                    batch_size=update_batch_size,
                    **bulk_update_kwargs
                )
            )

        if current_batch == 0:
            logger.info("{} has no records".format(model_name))

    def get_meta(self):
        meta = self.Meta()
        if not hasattr(meta, "select_chunk_size"):
            # Chunk size to iterate over
            meta.select_chunk_size = 5000
        if not hasattr(meta, "update_batch_size"):
            # Batch size for bulk updates
            meta.update_batch_size = 200
        return meta

    _meta = property(get_meta)

    def get_manager(self):
        meta = self._meta
        return getattr(meta, "manager", meta.model.objects)

    _manager = property(get_manager)

    def get_queryset(self):
        """ Override this if you want to delimit the objects that should be
            affected by anonymization
        """
        return self.get_manager().all()

    def patch_object(self, obj):
        """ Update object attributes with fake data provided by replacers
        """
        # using obj.__dict__ instead of getattr for performance reasons
        # see https://stackoverflow.com/a/9791053/639465
        fields = [field for field in self._declarations if obj.__dict__[field]]

        for field in fields:
            replacer = self._declarations[field]
            if isinstance(replacer, LazyAttribute):
                # Pass in obj for LazyAttributes
                new_value = replacer(obj)
            elif callable(replacer):
                new_value = replacer()
            else:
                new_value = replacer

            obj.__dict__[field] = new_value

        self.clean(obj)

    def clean(self, obj):
        """ Use this function if you need to update additional data that may
            rely on multiple fields, or if you need to update multiple fields
            at once
        """
        pass

    def get_declarations(self):
        """ Returns ordered declarations. Any non-ordered declarations, for
            example any types that does not inherit from OrderedDeclaration
            will come first, as they are considered "raw" values and should
            not be affected by the order of other non-ordered declarations
        """

        def _sort_declaration(declaration):
            name, value = declaration
            if isinstance(value, OrderedDeclaration):
                return value._order
            else:
                # Any non-ordered declarations come first
                return -1

        declarations = self._get_class_attributes().items()
        sorted_declarations = sorted(declarations, key=_sort_declaration)

        return OrderedDict(sorted_declarations)

    def _get_class_attributes(self):
        """ Return list of class attributes, which also includes methods and
            subclasses, ignoring any magic methods and reserved attributes
        """
        reserved_names = list(BaseAnonymizer.__dict__.keys()) + ["Meta"]

        return {
            name: self.__class__.__dict__[name]
            for name, value in self.__class__.__dict__.items()
            if not name.startswith("__") and name not in reserved_names
        }
