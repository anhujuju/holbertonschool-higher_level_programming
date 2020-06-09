#!/usr/bin/python3

"""
Unittest for base([..])

"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import json
import unittest


class TestBase(unittest.TestCase):
    """ class TestBase"""

    def test_base(self):
        """tests for base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertIsInstance(b1, Base)

        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertIsInstance(b2, Base)

        b3 = Base(9)
        self.assertEqual(b3.id, 9)
        self.assertIsInstance(b3, Base)

        b4 = Base()
        self.assertEqual(b4.id, 3)
        self.assertIsInstance(b4, Base)

        b5 = Rectangle(10, 7, 2, 8)
        dictionary = b5.to_dictionary()
        comdict = {'x': 2, 'width': 10, 'id': 4, 'height': 7, 'y': 8}
        self.assertDictEqual(dictionary, comdict)
        self.assertIn(Base.to_json_string([sorted(dictionary.items())]),
                      json.dumps([sorted(comdict.items())]))
        self.assertIsInstance(Base.to_json_string([dictionary]), str)

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

        with self.assertRaises(TypeError) as err:
            Base.to_json_string(5)
        self.assertEqual("argument must be a list of dictionaries",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Base.to_json_string("hello")
        self.assertEqual("argument must be a list of dictionaries",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Base.to_json_string((1,))
        self.assertEqual("argument must be a list of dictionaries",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Base.to_json_string({'Diva': 'Lei'})
        self.assertEqual("argument must be a list of dictionaries",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Base.to_json_string(True)
        self.assertEqual("argument must be a list of dictionaries",
                         str(err.exception))

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
                self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
                self.assertEqual(f.read(), "[]")


        Square.save_to_file([])
        with open("Square.json", "r") as f:
                self.assertEqual(f.read(), "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
                self.assertEqual(f.read(), "[]")

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file({'Diva': 'Lei'})
        self.assertEqual("argument must be a list of instances",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file(5)
        self.assertEqual("argument must be a list of instances",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file(False)
        self.assertEqual("argument must be a list of instances",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file("Diva")
        self.assertEqual("argument must be a list of instances",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file([4, 5])
        self.assertEqual("argument must be a list of instances" +
                         " who inherits of Base", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file([True, False])
        self.assertEqual("argument must be a list of instances" +
                         " who inherits of Base", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file(["sun", "moon", "star"])
        self.assertEqual("argument must be a list of instances" +
                         " who inherits of Base", str(err.exception))

        b6 = Base()
        b7 = Base()

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file([b6, b7])
        self.assertEqual("argument must be a list of instances" +
                         " who inherits of Base", str(err.exception))

        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])

        l_1 = {'id': 89, 'width': 10, 'height': 4}

        l_2 = Rectangle.to_json_string([l_1])
        self.assertIsInstance(l_2, str)

        l_3 = Rectangle.from_json_string(l_2)
        self.assertIsInstance(l_3, list)

        with self.assertRaises(TypeError) as err:
            Rectangle.from_json_string(6)
        self.assertEqual("argument must be a JSON string", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.from_json_string([1, 2])
        self.assertEqual("argument must be a JSON string", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.from_json_string(True)
        self.assertEqual("argument must be a JSON string", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.from_json_string((2, 6))
        self.assertEqual("argument must be a JSON string", str(err.exception))

        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)

        self.assertEqual(r2.__str__(), "[Rectangle] (7) 1/0 - 3/5")
        self.assertIsNot(r1, r2)

        with self.assertRaises(TypeError) as err:
            Rectangle.create(6)
        self.assertEqual("create() takes 1 positional argument" +
                         " but 2 were given", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.create(True)
        self.assertEqual("create() takes 1 positional argument" +
                         " but 2 were given", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.create("Hello")
        self.assertEqual("create() takes 1 positional argument" +
                         " but 2 were given", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle.create(r1_dict)
        self.assertEqual("create() takes 1 positional argument" +
                         " but 2 were given", str(err.exception))

        r3 = Rectangle(10, 7, 2, 8)
        r4 = Rectangle(2, 4)
        l_in = [r3, r4]
        Rectangle.save_to_file(l_in)
        l_out = Rectangle.load_from_file()

        self.assertEqual(l_out[0].__str__(), "[Rectangle] (9) 2/8 - 10/7")
        self.assertEqual(l_out[1].__str__(), "[Rectangle] (10) 0/0 - 2/4")

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        ls_in = [s1, s2]

        Square.save_to_file(ls_in)
        ls_out = Square.load_from_file()

        self.assertEqual(ls_out[0].__str__(), "[Square] (13) 0/0 - 5")
        self.assertEqual(ls_out[1].__str__(), "[Square] (14) 9/1 - 7")

        with self.assertRaises(NameError) as err:
            Diva.load_from_file()
        self.assertEqual("name 'Diva' is not defined", str(err.exception))

if __name__ == '__main__':
    unittest.main()
#
