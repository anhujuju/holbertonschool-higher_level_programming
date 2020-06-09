#!/usr/bin/python3

"""
Unittest for base([..])

"""

from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib
import unittest


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""
    def test_rectangle(self):
        """Tests for Rectangle class"""
        r1 = Rectangle(10, 2)
#        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

        r2 = Rectangle(2, 10, 5)
#        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 0)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsInstance(r2, Base)

        r3 = Rectangle(10, 2, 2, 3, 12)
#       self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 3)
        self.assertIsInstance(r3, Rectangle)
        self.assertIsInstance(r3, Base)

        r4 = Rectangle(10, 2)
        self.assertEqual(r4.area(), 20)

        r5 = Rectangle(2, 3, 1)
        self.assertEqual(r5.area(), 6)
        sdio = io.StringIO()
        with contextlib.redirect_stdout(sdio):
            r5.display()
        self.assertEqual(sdio.getvalue(), " ##\n ##\n ##\n")

        r6 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(r6.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r6.update(89)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 2/1 - 4/6")

        r6.update(89, 2)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 2/1 - 2/6")

        r6.update(89, 2, 3)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 2/1 - 2/3")

        r6.update(89, 2, 3, 4)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 4/1 - 2/3")

        r6.update(89, 2, 3, 4, 5)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        with self.assertRaises(ValueError) as err:
            r6.update(5, -10)
        self.assertEqual("width must be > 0", str(err.exception))

        r7 = Rectangle(5, 5, 1, 0, 5)
        self.assertEqual(r7.__str__(), '[Rectangle] (5) 1/0 - 5/5')

        r8 = Rectangle(2, 4, 0, 0, 6)
        self.assertEqual(r8.__str__(), '[Rectangle] (6) 0/0 - 2/4')

        r9 = Rectangle(10, 10, 10, 10, 7)
        self.assertEqual(r9.__str__(), "[Rectangle] (7) 10/10 - 10/10")

        r9.update(diva=20, id=7)
        self.assertEqual(r9.__str__(), "[Rectangle] (7) 10/10 - 10/10")

        r9.update(height=1, id=7)
        self.assertEqual(r9.__str__(), "[Rectangle] (7) 10/10 - 10/1")

        r9.update(width=1, x=2)
        self.assertEqual(r9.__str__(), "[Rectangle] (7) 2/10 - 1/1")

        r9.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 3/1 - 2/1")

        r9.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 1/3 - 4/2")

        with self.assertRaises(ValueError) as err:
            r6.update(width=-10)
        self.assertEqual("width must be > 0", str(err.exception))

        r10 = Rectangle(10, 2, 1, 9, 8)
        new_dict = {'width': 10, 'height': 2, 'id': 8, 'x': 1, 'y': 9}
        self.assertEqual(r10.to_dictionary(), new_dict)
        self.assertEqual(r10.__str__(), "[Rectangle] (8) 1/9 - 10/2")
        self.assertIsInstance(r10.to_dictionary(), dict)
        self.assertIsInstance(r10, Rectangle)

        r11 = Rectangle(1, 1)
        r11.update(**r10.to_dictionary())
        self.assertEqual(r11.__str__(), "[Rectangle] (8) 1/9 - 10/2")
        self.assertFalse(r11 == r10)

        r12 = Rectangle(1, 2, 0, 0, 10)
        new_dict2 = {'width': 1, 'height': 2, 'id': 10, 'x': 0, 'y': 0}
        self.assertEqual(r12.to_dictionary(), new_dict2)

        sdio = io.StringIO()
        with contextlib.redirect_stdout(sdio):
            r12.display()
        self.assertEqual(sdio.getvalue(), "#\n#\n")

        # no arguments
        with self.assertRaises(TypeError) as err:
            Rectangle()
        self.assertEqual("__init__() missing 2 required positional " +
                         "arguments: 'width' and 'height'", str(err.exception))

        # TypeError for height
        with self.assertRaises(TypeError) as err:
            Rectangle(10, "10")
        self.assertEqual("height must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, True)
        self.assertEqual("height must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, {})
        self.assertEqual("height must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, [])
        self.assertEqual("height must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, (10,))
        self.assertEqual("height must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10.5)
        self.assertEqual("height must be an integer", str(err.exception))

        # TypeError for width
        with self.assertRaises(TypeError) as err:
            Rectangle("10", 10)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(False, 10)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle({}, 10)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle([], 10)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(5.5, 10)
        self.assertEqual("width must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle((5,), 10)
        self.assertEqual("width must be an integer", str(err.exception))

        # TypeError for x
        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, "5", 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, True, 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, {}, 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, [], 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, (), 7)
        self.assertEqual("x must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5.27, 7)
        self.assertEqual("x must be an integer", str(err.exception))

        # TypeError for y
        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5, "7")
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5, False)
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5, {})
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5, [])
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5, ())
        self.assertEqual("y must be an integer", str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, 5, 1.78)
        self.assertEqual("y must be an integer", str(err.exception))

        # ValueError for height
        with self.assertRaises(ValueError) as err:
            Rectangle(10, -10)
        self.assertEqual("height must be > 0", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(10, 0)
        self.assertEqual("height must be > 0", str(err.exception))

        # ValueError for width
        with self.assertRaises(ValueError) as err:
            Rectangle(-10, 10)
        self.assertEqual("width must be > 0", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(0, 10)
        self.assertEqual("width must be > 0", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(0, 0)
        self.assertEqual("width must be > 0", str(err.exception))

        # ValueError for x
        with self.assertRaises(ValueError) as err:
            Rectangle(10, 10, -10)
        self.assertEqual("x must be >= 0", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(10, 10, -10, -10)
        self.assertEqual("x must be >= 0", str(err.exception))

        # ValueError for y
        with self.assertRaises(ValueError) as err:
            Rectangle(10, 10, 10, -10)
        self.assertEqual("y must be >= 0", str(err.exception))

if __name__ == '__main__':
    unittest.main()
#
