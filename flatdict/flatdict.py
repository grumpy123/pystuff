class FlatDict(object):
    def __init__(self, fetcher):
        self._fetcher = fetcher
        self._ = CacheCleaner(self)

    def __getattr__(self, item):
        val = self._fetcher(item)
        setattr(self, item, val)
        return val


class CacheCleaner(object):
    def __init__(self, fd):
        self.fd = fd

    def __getattr__(self, item):
        try:
           delattr(self.fd, item)
        except AttributeError:
            pass

        return getattr(self.fd, item)

