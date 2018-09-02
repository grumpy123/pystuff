from collections import OrderedDict, namedtuple


Required = object()


def tuple_factory(_tuple_name, tuple_req=None, **kwargs):
    required = []
    if tuple_req:
        required = tuple_req
        if isinstance(required, str):
            required = required.split()
    required += list(kwargs.keys())
    defaults = {k: v for k, v in kwargs.items() if v is not Required}
    T = namedtuple(_tuple_name, required)

    def _factory(*args, **kwargs):
        for field, val in zip(T._fields, args):
            kwargs[field] = val
        for field, default_val in defaults.items():
            if field not in kwargs:
                kwargs[field] = default_val
        return T(**kwargs)

    return _factory