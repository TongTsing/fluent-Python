import collections
from collections import abc
import keyword

class FrozenJSON(object):
    def __init__(self, mapping: collections.abc.Mapping):
        self._data = {}
        # 处理关键字冲突
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self._data[key] = value

    def __getattr__(self, name):
        # 处理关键字冲突
        if keyword.iskeyword(name):
            name += '_'

        try:
            value = getattr(self._data, name)
        except AttributeError:
            pass

        try:
            value = self._data[name]
        except KeyError:
            raise AttributeError(f"No such attribute: {name}")
        
        return self.build(value)

    @classmethod 
    def build(cls, obj):
        if isinstance(obj, collections.abc.Mapping):
            return FrozenJSON(obj)
        elif isinstance(obj, collections.abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj