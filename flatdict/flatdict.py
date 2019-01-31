class FlatDict(object):
    def __init__(self, fetcher):
        self._fetcher = fetcher

    def __getattr__(self, item):
        return self._fetcher(item)