import collections
from collections import abc

class FrozenJSON(object):
    def __init__(self, mapping: collections.abc.Mapping):
        self._data = mapping

    def __getattr__(self, item):
        try:
            return getattr(self._data, item)
        except AttributeError:
            raise AttributeError(item)