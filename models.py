from collections import OrderedDict
from manager import Manager


class Field:
    pass


class IntegerField(Field):
    pass


class CharField(Field):
    pass


class ModelMeta(type):
    def __new__(mcs, class_name, parents, attributes):
        fields = OrderedDict()
        for k, v in attributes.items():
            if isinstance(v, Field):
                fields[k] = v
                attributes[k] = None
        h = super(ModelMeta, mcs).__new__(mcs, class_name, parents, attributes)
        setattr(h, '_model_name', attributes['__qualname__'].lower())
        setattr(h, '_original_fields', fields)
        setattr(h, 'objects', Manager(h))
        return h


class Model(metaclass=ModelMeta):
    pass
