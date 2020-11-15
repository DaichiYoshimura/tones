class MapperMixIn(dict):

    def key_of(self, value, default=None):
        return self._switch(self.items()).get(value, default)

    def value_of(self, key, default=None):
        return self.get(key, default)

    def key_list(self):
        return list(self.keys())

    def value_list(self):
        return list(self.values())

    def _switch(self, target):
        return {v: k for k, v in target}
    
    
