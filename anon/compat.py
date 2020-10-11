# deps
from django_bulk_update.helper import bulk_update as ext_bulk_update


def bulk_update(objects, manager, **bulk_update_kwargs):
    """Updates the list of objects using django queryset's
    inbuilt ``.bulk_update()`` method if present, else
    django_bulk_update's ``bulk_update()`` will be used

    :param objects: list of objects that needs to be bulk updated
    :type objects: list[object]
    :param manager: instance of django model manager
    :type manager: models.Manager
    :param bulk_update_kwargs: keyword arguments passed to the ``bulk_update()``
    :return: None
    :rtype: None
    """
    try:
        manager.bulk_update(objects, **bulk_update_kwargs)
    except AttributeError:
        ext_bulk_update(objects, **bulk_update_kwargs)
