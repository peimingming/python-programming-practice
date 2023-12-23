# Built-in Functions: https://docs.python.org/3/library/functions.html.

# var1 = input("Please input the first var: ")
# var2 = input("Please input the second var: ")
# print(f"var2 = {var2}")
# print(f"var1 = {var1}")

# x = 1
# y = "Hello"
# print(x)
# print(y)
#
# a, b = 1, 2
# print(a, b)

# x = 1234
# z = y = x
# print(x, y, z)
# x = 4321
# print(x, y, z)


# String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods.

# a = 'Hello'
# b = "Hello"
# c = '''Hello'''
# c1 = '''
# How are you doing?
# '''
# d = """Hello"""
# d1 = """
# How are "you" doing?
# """
# d2 = '\nHow are "you" doing?\n'
# print(a, b, c, d)
# print(c1)
# print(d1)
# print(d2)
# print(d1 is d2)
# print(f"{a}, {b}, {c}, {d}")

# s = "I am a string"
# print("am" in s)
# print("am" not in s)

# x = "abc"
# y = "xyz"
# print(x + y)
# print(x * 3)
# print(x, y)

# s = "123456"
# print(s[0])
# print(s[-1])
# print(s[0:3])
# print(s[0:3:2])

# s = "123456"
# print(s.count("12"))
# print(s.isalnum())
# print(s.isalpha())
# print(s.join("abc"))
# print(s.split(","))
# print(s.startswith("123"))

# print("xyzxyzxyz".count("xyz"))
# print("xyzxyzxyz".count("a"))
# print("xyzxyzxyz".isalnum())
# print("xyzxyzxyz".isalpha())
# print(",".join("abcdefg"))
# print("a,b,c,d".split(","))
# print("xyz".startswith("x"))


# Number Types: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex.

# print(type(123))
# print(type(123.456))
# print(type("123"))
# print(int(123.456))
# print(float(123))
# print(int("123"))
# print(float("123.456"))
# print(float("123"))
# abc = 123
# print(type(abc))
# abc = "abc"
# print(type(abc))


# String & Number.

# print(100 + 300)
# print("100" + "300")
# print(456 > 1234)
# print("456" > "1234")
# print(len("456") > len("1234"))
# print(123 > 123.456)


# Calculator.

# number1 = int(input("Please input the 1st number: "))
# number2 = int(input("Please input the 2nd number: "))
# operand = input("Please input the operand (+ - * /): ")
# result = eval(f"{number1}{operand}{number2}")
# print(f"{number1} {operand} {number2} = {result}")


# Annotations: https://peps.python.org/pep-0020/#the-zen-of-python.

# # The type of the input is 'str'.
# age = input("Please input your age: ")
# print(age, type(age))
# age = int(age)  # age is 'int' now.
# print(age, type(age))


# Python Coding Standards: https://peps.python.org/pep-0008/#introduction.
