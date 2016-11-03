try:
    # Python 3
    from unittest import mock

except ImportError:
    # Python 2
    import mock

patch = mock.patch
