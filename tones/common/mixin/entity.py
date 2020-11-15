class EntityMixIn:
    

    def get_public_property(self)-> list:
        public_attr = []
        for x in self.__dict__.keys():
            if str(x) not in '_':
                public_attr.append(x)
        return public_attr
