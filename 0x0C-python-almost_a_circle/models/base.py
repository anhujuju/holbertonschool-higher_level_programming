#!/usr/bin/python3

"""
Base class
"""
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """from list of dict to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("argument must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of instances to file"""
        with open('{}.json'.format(cls.__name__), 'w') as f:
            if list_objs is None or list_objs == []:
                f.write(cls.to_json_string([]))
                return
            if not isinstance(list_objs, list):
                raise TypeError("argument must be a list of instances")
            for x in list_objs:
                if not isinstance(x, Base) or type(x) == Base:
                    raise TypeError("argument must be a list" +
                                    " of instances who inherits of Base")
            else:
                di = []
                for obj in list_objs:
                    obj = obj.to_dictionary()
                    di.append(obj)
                f.write(cls.to_json_string(di))

    @staticmethod
    def from_json_string(json_string):
        """from json string to list"""
        if json_string is None or json_string == "":
            return []
        if not isinstance(json_string, str):
            raise TypeError("argument must be a JSON string")
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create instance of all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if not isinstance(dictionary, dict):
            raise TypeError("argument must be a dictionary")

        if cls.__name__ == "Rectangle":
            c = Rectangle(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            c = Square(1, 0, 0)
        c.update(**dictionary)
        return c

    @classmethod
    def load_from_file(cls):
        """load list of instances from file"""
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                cont = f.read()
            new = []
            for obj in cls.from_json_string(cont):
                new.append(cls.create(**obj))
            return new
        except FileNotFoundError:
            return []
