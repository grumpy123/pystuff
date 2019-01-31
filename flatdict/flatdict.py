class FlatDict(object):
    def __init__(self, fetcher):
        self._fetcher = fetcher

    def __getattr__(self, item):
        val = self._fetcher(item)
        setattr(self, item, val)
        return val
