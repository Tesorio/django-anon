try:
    # stdlib
    from unittest import mocka  # noqa: F401
except ImportError:
    # deps
    import mock  # noqa: F401
