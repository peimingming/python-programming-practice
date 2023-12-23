# Basics

## Input & Output

Refer to [Built-in Functions](https://docs.python.org/3/library/functions.html).

1. `input` & `print`:

   ```python
   var1 = input("Please input the first var: ")
   print(var1)
   print(f"var1 = {var1}")
   ```

2. assignments:

   ```python
   a, b = 1, 2
   print(a, b)
   
   x = 1234
   z = y = x
   print(x, y, z)
   ```

## Strings

Refer to [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

1. `a`, `b`, `c`, `d` are the same strings - `Hello`, it's up to the specific scenario to use the correspondng way to express strings:

   ```python
   a = 'Hello'
   b = "Hello"
   c = '''Hello'''
   d = """Hello"""
   print(a, b, c, d)
   ```

2. `in` & `not in`:

   ```python
   s = "I am a string"
   print("am" in s)
   print("am" not in s)
   ```

3. `+` & `*`:

   ```python
   x = "abc"
   y = "xyz"
   print(x + y)  # abcxyz
   print(x * 3)  # abcabcabc
   ```

4. `s[i:j:k]`:

   ```python
   s = "123456"
   print(s[0])  # 1
   print(s[-1])  # 6
   print(s[0:3])  # 123
   print(s[0:3:2])  # 13
   ```

5. `s.x`:

   ```python
   s = "123456"
   print(s.count("12"))  # 1
   print(s.isalnum())  # True
   print(s.isalpha())  # False
   print(s.join("abc"))  # a123456b123456c
   print(s.split(","))  # ['123456']
   print(s.startswith("123"))  # True
   ```

## Numbers

Refer to [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

1. `type()`:

   ```python
   print(type(123))  # <class 'int'>
   print(type(123.456))  # <class 'float'>
   ```

2. assignments (type of `abc` could be changed in runtime):

   ```python
   abc = 123
   print(type(abc))  # <class 'int'>
   abc = "abc"
   print(type(abc))  # <class 'str'>
   ```

3. a simple calculator:

   ```python
   number1 = int(input("Please input the 1st number: "))
   number2 = int(input("Please input the 2nd number: "))
   operand = input("Please input the operand (+ - * /): ")
   result = eval(f"{number1}{operand}{number2}")
   print(f"{number1} {operand} {number2} = {result}")
   ```

## The Zen of Python

https://peps.python.org/pep-0020/#the-zen-of-python

## Python Coding Standards

https://peps.python.org/pep-0008/#introduction
