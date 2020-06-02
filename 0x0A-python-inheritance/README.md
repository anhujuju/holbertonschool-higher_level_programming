# Python - Inheritance

Python scripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [Python 3.4.3](https://www.python.org/downloads/release/python-343/) and must conform to [PEP 8 (v1.7.x)](https://pep8.readthedocs.io/en/release-1.7.x/intro.html) style.

### Focus
Learn how to create parent and child classes in Python to perform the concept of inheritance. How to write tests and execute them using Python's `doctest` module.

### Example Usages

[0-lookup.py](0-lookup.py)
```
0x0A-python-inheritance:$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
0x0A-python-inheritance:$ 
```
[1-my_list.py](1-my_list.py)
```
0x0A-python-inheritance:$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
0x0A-python-inheritance:$ 
```
[2-is_same_class.py](2-is_same_class.py)
```
0x0A-python-inheritance:$ ./2-main.py
1 is an instance of the class int
0x0A-python-inheritance:$ 
```
[3-is_kind_of_class.py](3-is_kind_of_class.py)
```
0x0A-python-inheritance:$ ./3-main.py
1 comes from int
1 comes from object
0x0A-python-inheritance:$ 
```
[4-inherits_from.py](4-inherits_from.py)
```
0x0A-python-inheritance:$ ./4-main.py
True inherited from class int
True inherited from class object
0x0A-python-inheritance:$ 
```
[5-base_geometry.py](5-base_geometry.py)
```
0x0A-python-inheritance:$ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
0x0A-python-inheritance:$ 
```
[6-base_geometry.py](6-base_geometry.py)
```
0x0A-python-inheritance:$ ./6-main.py
[Exception] area() is not implemented
0x0A-python-inheritance:$ 
```
[7-base_geometry.py](7-base_geometry.py)
```
0x0A-python-inheritance:$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
0x0A-python-inheritance:$ 
```
[8-rectangle.py](8-rectangle.py)
```
0x0A-python-inheritance:$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
0x0A-python-inheritance:$ 
```
[9-rectangle.py](9-rectangle.py)
```
0x0A-python-inheritance:$ ./9-main.py
[Rectangle] 3/5
15
0x0A-python-inheritance:$ 
```
[10-square.py](10-square.py)
```
0x0A-python-inheritance:$ ./10-main.py
[Rectangle] 13/13
169
0x0A-python-inheritance:$ 
```
[11-square.py](11-square.py)
```
0x0A-python-inheritance:$ ./11-main.py
[Square] 13/13
169
0x0A-python-inheritance:$ 
```
[100-my_int.py](100-my_int.py)
```
0x0A-python-inheritance:$ ./100-main.py
3
False
True
0x0A-python-inheritance:$ 
```
[101-add_attribute.py](101-add_attribute.py)
```
0x0A-python-inheritance:$ ./101-main.py
John
[TypeError] can't add new attribute
0x0A-python-inheritance:$ 
```
### Author
- [Alex Yu](https://github.com/AlexYu01)
### Acknowledgments
- [Holberton](https://www.holbertonschool.com/)
