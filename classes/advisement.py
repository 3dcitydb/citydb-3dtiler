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

class Advice(TransformedDict):
    def __init__(self, commandset, recommended_mft=None, namespaces=None, crs_code=None):
        super().__init__()
        self.store["commandset"] = commandset
        self.store["recommended_mft"] = recommended_mft
        self.store["namespaces"] = namespaces
        self.store["used_crs_code"] = crs_code
    def _keytransform(self, key):
        return key.lower()

class Namespace(TransformedDict):
    def __init__(self, alias, recommended_mft=None, objectclasses=None):
        super().__init__()
        self.store["alias"] = alias
        # self.store["exact_name"] = exact_name
        if recommended_mft != None:
            self.store["recommended_mft"] = recommended_mft
        if objectclasses != None:
            self.store["objectclasses"] = objectclasses

class ObjectClass(TransformedDict):
    # Info : "objectclass_recommendations" replaced with "recommended_mft"
    def __init__(self, name, recommended_mft=None, properties=None):
        super().__init__()
        self.store["name"] = name
        if recommended_mft != None:
            self.store["recommended_mft"] = recommended_mft
        if properties != None:
            self.store["properties"] = properties

class ObjectClassRecommendations(TransformedDict):
    def __init__(self, max_features):
        super().__init__()
        self.store["max_features"] = max_features

