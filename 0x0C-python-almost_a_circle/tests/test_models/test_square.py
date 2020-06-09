#!/usr/bin/python3

"""
Unittest for base([..])

"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib
import unittest


class TestSquare(unittest.TestCase):
    """class TestSquare"""
    def test_square(self):
        """tests for Square class"""
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.area(), 25)
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s1, Rectangle)
        self.assertIsInstance(s1, Base)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

        s2 = Square(2, 10, 0, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 10)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.area(), 4)
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Rectangle)
        self.assertIsInstance(s2, Base)
        self.assertEqual(s2.__str__(), "[Square] (2) 10/0 - 2")

        s3 = Square(9, 15, 5, 20)
        self.assertEqual(s3.size, 9)
        self.assertEqual(s3.width, 9)
        self.assertEqual(s3.height, 9)
        self.assertEqual(s3.x, 15)
        self.assertEqual(s3.y, 5)
        self.assertEqual(s3.area(), 81)
        self.assertIsInstance(s3, Square)
        self.assertIsInstance(s3, Rectangle)
        self.assertIsInstance(s3, Base)
        self.assertEqual(s3.__str__(), "[Square] (20) 15/5 - 9")

        s3.update(89)
        self.assertEqual(s3.__str__(), "[Square] (89) 15/5 - 9")

        s3.update(89, 2)
        self.assertEqual(s3.__str__(), "[Square] (89) 15/5 - 2")

        s3.update(89, 2, 3)
        self.assertEqual(s3.__str__(), "[Square] (89) 3/5 - 2")

        s3.update(89, 2, 3, 4)
        self.assertEqual(s3.__str__(), "[Square] (89) 3/4 - 2")

        with self.assertRaises(ValueError) as err:
            s3.update(1, -10)
        self.assertEqual("width must be > 0", str(err.exception))

        s4 = Square(5, 5, 1, 3)
        self.assertEqual(s4.__str__(), '[Square] (3) 5/1 - 5')

        s4.update(diva=20)
        self.assertEqual(s4.__str__(), '[Square] (3) 5/1 - 5')

        s4.update(size=1)
        self.assertEqual(s4.__str__(), '[Square] (3) 5/1 - 1')

        s4.update(size=7, x=2)
        self.assertEqual(s4.__str__(), '[Square] (3) 2/1 - 7')

        s4.update(y=1, x=3, id=89)
        self.assertEqual(s4.__str__(), '[Square] (89) 3/1 - 7')

        with self.assertRaises(ValueError) as err:
            s4.update(size=-10)
        self.assertEqual("width must be > 0", str(err.exception))

        s5 = Square(10, 2, 1, 4)
        new_dict = {'size': 10, 'id': 4, 'x': 2, 'y': 1}
        self.assertEqual(s5.to_dictionary(), new_dict)
        self.assertEqual(s5.__str__(), "[Square] (4) 2/1 - 10")
        self.assertIsInstance(s5.to_dictionary(), dict)
        self.assertIsInstance(s5, Square)

        s6 = Square(1, 1)
        sdio = io.StringIO()
        with contextlib.redirect_stdout(sdio):
            s6.display()
        self.assertEqual(sdio.getvalue(), " #\n")

        s6.update(**s5.to_dictionary())
        self.assertEqual(s6.__str__(), "[Square] (4) 2/1 - 10")
        self.assertFalse(s6 == s5)

        s7 = Square(1, 0, 0, 6)
        new_dict2 = {'size': 1, 'id': 6, 'x': 0, 'y': 0}
        self.assertEqual(s7.to_dictionary(), new_dict2)

        s8 = Square(3, 2)
        sdio = io.StringIO()
        with contextlib.redirect_stdout(sdio):
            s8.display()
        self.assertEqual(sdio.getvalue(), "  ###\n  ###\n  ###\n")

        # no arguments
        with self.assertRaises(TypeError) as err:
            Square()
        self.assertEqual("__init__() missing 1 required positional " +
                         "argument: 'size'", str(err.exception))

        # TypeError for size
        with self.assertRaises(TypeError) as err:
            Square("10")
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(False)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square({})
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square([])
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(5.5)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square((5,))
        self.assertEqual("width must be an integer", str(err.exception))

        # TypeError for x
        with self.assertRaises(TypeError) as err:
            Square(10, "5", 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, True, 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, {}, 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, [], 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, (), 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, 5.27, 7)
        self.assertEqual("x must be an integer", str(err.exception))

        # TypeError for y
        with self.assertRaises(TypeError) as err:
            Square(10, 5, "7")
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, 5, False)
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, 5, {})
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, 5, [])
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, 5, ())
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Square(10, 5, 1.78)
        self.assertEqual("y must be an integer", str(err.exception))

        # ValueError for width
        with self.assertRaises(ValueError) as err:
            Square(-10)
        self.assertEqual("width must be > 0", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Square(0)
        self.assertEqual("width must be > 0", str(err.exception))

        # ValueError for x
        with self.assertRaises(ValueError) as err:
            Square(10, -10)
        self.assertEqual("x must be >= 0", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Square(10, -10, -10)
        self.assertEqual("x must be >= 0", str(err.exception))

        # ValueError for y
        with self.assertRaises(ValueError) as err:
            Square(10, 10, -10)
        self.assertEqual("y must be >= 0", str(err.exception))

if __name__ == '__main__':
    unittest.main()
#
