from collections.abc import MutableMapping

class TransformedDict(MutableMapping):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[self._keytransform(key)]

    def __setitem__(self, key, value):
        self.store[self._keytransform(key)] = value

    def __delitem__(self, key):
        del self.store[self._keytransform(key)]

    def __iter__(self):
        return iter(self.store)
    
    def __len__(self):
        return len(self.store)

    def __repr__(self):
        return str(self.store)

    def _keytransform(self, key):
        return key

class Advisement(TransformedDict):
    def __init__(self, commandset, max_features=None, objectclasses=None, crs_code=None):
        super().__init__()
        self.store["commandset"] = commandset
        self.store["max_features"] = max_features
        self.store["objectclasses"] = objectclasses
        self.store["used_crs_code"] = crs_code
    def _keytransform(self, key):
        return key.lower()

class ObjectClass(TransformedDict):
    def __init__(self, name, objectclass_recommendations=None, properties=None):
        super().__init__()
        self.store["name"] = name
        if objectclass_recommendations != None:
            self.store["objectclass_recommendations"] = objectclass_recommendations
        if properties != None:
            self.store["properties"] = properties

class ObjectClassRecommendations(TransformedDict):
    def __init__(self, max_features):
        super().__init__()
        self.store["max_features"] = max_features

