d = {
    'a':100,
    'name': 'jexx'
}

class DictObj:
    def __init__(self, d:dict):
        if isinstance(d, dict):
            self.__dict__['_dict'] = d
        else:
            self.__dict__['_dict'] = {}

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError('Attribute {} Not Found'.format(item))

    def __setattr__(self, key, value):
        #self._dict[key] = value
        # 不允许设置属性
        raise NotImplementedError

do = DictObj(d)
print(do.name)
print(do.a)

