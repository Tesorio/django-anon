from django_bulk_update.helper import bulk_update as ext_bulk_update


def bulk_update(objects, manager, **bulk_update_kwargs):
    """ Updates the list of objects using django queryset's
        inbuilt `.bulk_update()` method if present, else
        django_bulk_update's `bulk_update` will be used
    """
    if getattr(manager, "bulk_update", None):
        manager.bulk_update(objects, **bulk_update_kwargs)
    else:
        ext_bulk_update(objects, bulk_update_kwargs)
