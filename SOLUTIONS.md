# Solutions and Explanations for Python Challenges

This document provides the answers and logic behind the 50 problem-solving challenges.

---

## Section 1: Beginner Foundations

### 1. Greeting App
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
years_to_100 = 100 - age
print(f"Hello {name}! You have {years_to_100} years until you turn 100.")
```
**Explanation:** We use `input()` to get data from the user. Since `input()` returns a string, we must cast `age` to an `int` to perform subtraction.

### 2. String Reverser
```python
def reverse_string(s):
    return s[::-1]
```
**Explanation:** Slicing `[start:stop:step]` with a step of `-1` is the most idiomatic way to reverse a string in Python.

### 3. List Calculator
```python
nums = [10, 20, 30, 40, 50]
total = 0
largest = nums[0]
for n in nums:
    total += n
    if n > largest:
        largest = n
avg = total / len(nums)
print(f"Sum: {total}, Avg: {avg}, Max: {largest}")
```
**Explanation:** We iterate through the list manually, maintaining a running total and updating the `largest` variable if we find a bigger number.

### 4. Unique Elements
```python
def get_unique(items):
    return list(set(items))
```
**Explanation:** Sets automatically remove duplicates. Converting a list to a set and back to a list is an efficient way to find unique values.

### 5. Dictionary Lookup
```python
capitals = {"USA": "DC", "France": "Paris", "India": "Delhi"}
country = input("Country: ")
print(capitals.get(country, "Not Found"))
```
**Explanation:** The `.get()` method is safer than `dict[key]` because it returns a default value instead of raising a `KeyError` if the key is missing.

### 6. Case Swapper
```python
text = "Hello World"
print(text.swapcase())
```
**Explanation:** Python strings have a built-in `.swapcase()` method that handles this exact task.

### 7. List Slicer
```python
nums = list(range(10))
print("First 3:", nums[:3])
print("Last 3:", nums[-3:])
print("Middle 4:", nums[3:7])
```
**Explanation:** Slicing allows accessing sub-parts of a list. `[:3]` starts at index 0, `[-3:]` goes from 3 from the end to the end.

### 8. Word Counter
```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Word count: {len(words)}")
```
**Explanation:** `.split()` breaks a string into a list of words based on whitespace. `len()` then counts the items in that list.

### 9. Type Checker
```python
def check_type(val):
    print(f"Type of {val} is {type(val)}")
```
**Explanation:** The built-in `type()` function returns the class/type of an object.

### 10. F-String Practice
```python
item, price, qty = "Apple", 0.5, 10
print(f"Item: {item}, Total: ${price * qty:.2f}")
```
**Explanation:** F-strings allow embedding expressions inside `{}` and support formatting, like `:.2f` for two decimal places.

---

## Section 2: Control Flow & Functions

### 11. Even/Odd Loop
```python
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i}: Even")
    else:
        print(f"{i}: Odd")
```
**Explanation:** The modulo operator `%` gives the remainder. If `i % 2` is 0, the number is even.

### 12. FizzBuzz
```python
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
**Explanation:** Order matters! Check for the combined condition (`% 3` and `% 5`) first, otherwise the separate conditions will trigger prematurely.

### 13. Prime Checker
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
**Explanation:** We check for factors up to the square root of `n`. If no factors are found, the number is prime.

### 14. Args Summation
```python
def multiply_all(*args):
    result = 1
    for n in args:
        result *= n
    return result
```
**Explanation:** `*args` collects any number of positional arguments into a tuple, which we then iterate over.

### 15. Area Calculator
```python
def get_area(shape, **kwargs):
    if shape == "circle":
        return 3.14 * (kwargs['radius']**2)
    elif shape == "rect":
        return kwargs['w'] * kwargs['h']
```
**Explanation:** `**kwargs` allows us to pass named arguments like `radius=5` or `w=10, h=5` dynamically.

### 16. LEGB Scope Demo
```python
x = "global"
def func():
    global x
    x = "modified"
func()
print(x) # Prints "modified"
```
**Explanation:** Local, Enclosing, Global, Built-in. The `global` keyword tells Python to use the variable from the global scope instead of creating a local one.

### 17. Lambda Filter
```python
ages = [12, 25, 18, 40, 10]
adults = list(filter(lambda x: x >= 18, ages))
```
**Explanation:** `filter()` takes a function (here a `lambda`) and an iterable, returning only items where the function returns `True`.

### 18. Recursive Factorial
```python
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)
```
**Explanation:** A function that calls itself with a base case (`n == 1`) to prevent infinite recursion.

### 19. Vowel Remover
```python
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([char for char in s if char not in vowels])
```
**Explanation:** We use a list comprehension to filter characters and `.join()` to turn the resulting list back into a string.

### 20. Dictionary Comprehension
```python
nums = [1, 2, 3, 4, 5, 6]
squares = {x: x**2 for x in nums if x % 2 == 0}
```
**Explanation:** Similar to list comprehensions but with `{key: value}` syntax.

---

## Section 3: Modules & Standard Library

### 21. OS Explorer
```python
import os
for file in os.listdir('.'):
    print(f"{file}: {os.path.getsize(file)} bytes")
```
**Explanation:** `os.listdir` lists filenames, and `os.path.getsize` provides their size in bytes.

### 22. Random Password
```python
import random, string
chars = string.ascii_letters + string.digits + string.punctuation
pwd = "".join(random.choice(chars) for _ in range(12))
```
**Explanation:** `random.choice` picks a single character. We repeat this 12 times and join them.

### 23. Days Until Birthday
```python
from datetime import date
today = date.today()
bday = date(today.year, 12, 25) # Assume Dec 25
if bday < today:
    bday = date(today.year + 1, 12, 25)
print((bday - today).days)
```
**Explanation:** Subtracting two `date` objects returns a `timedelta` object, which has a `.days` attribute.

### 24. Permutation Generator
```python
from itertools import permutations
perms = [''.join(p) for p in permutations("CODE")]
```
**Explanation:** `itertools.permutations` generates all possible orderings of the input iterable.

### 25. JSON Parser
```python
import json
data = '{"name": "John", "city": "NY"}'
d = json.loads(data)
d['city'] = 'LA'
new_json = json.dumps(d)
```
**Explanation:** `json.loads` converts string to dict; `json.dumps` converts dict back to string.

### 26. CSV Filter
```python
import csv
with open('scores.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Score']) > 80:
            print(row['Name'])
```
**Explanation:** `DictReader` maps the header row to keys in a dictionary for each subsequent row.

### 27. Math Constants
```python
import math
area = math.pi * (5**2)
```
**Explanation:** The `math` module provides high-precision constants like `pi` and `e`.

### 28. Zip & Map
```python
names = ["A", "B"]
ages = [20, 30]
zipped = list(zip(names, ages))
months = list(map(lambda x: x * 12, ages))
```
**Explanation:** `zip` pairs elements from multiple lists. `map` applies a function to every item in an iterable.

### 29. Sys Arguments
```python
import sys
if len(sys.argv) > 1:
    print(f"Hello {sys.argv[1]}")
```
**Explanation:** `sys.argv` is a list where the first element is the script name and subsequent elements are arguments passed in the terminal.

### 30. Counter Tool
```python
from collections import Counter
text = "sample text with many characters"
count = Counter(text)
print(count.most_common(1))
```
**Explanation:** `Counter` is a dictionary subclass for counting hashable objects.

---

## Section 4: OOP & Advanced Features

### 31. Employee Class
```python
class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def apply_raise(self):
        self.pay *= 1.05
```
**Explanation:** `__init__` is the constructor. `self` refers to the specific instance of the class.

### 32. Inheritance
```python
class Developer(Employee):
    def __init__(self, name, pay, prog_lang):
        super().__init__(name, pay)
        self.prog_lang = prog_lang
```
**Explanation:** `super()` calls the parent class's methods (like `__init__`), avoiding code duplication.

### 33. Dunder Methods
```python
class Employee:
    # ...
    def __repr__(self):
        return f"Employee('{self.name}', {self.pay})"
    def __str__(self):
        return f"{self.name} - {self.pay}"
```
**Explanation:** `__repr__` is for developers (debugging), `__str__` is for end-users (display).

### 34. Property Decorators
```python
class Employee:
    @property
    def email(self):
        return f"{self.name}@email.com"
```
**Explanation:** `@property` allows a method to be accessed like an attribute (no `()` needed).

### 35. Generator Expression
```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```
**Explanation:** `yield` pauses the function and returns a value, resuming from the same spot next time it's called. This is memory efficient.

### 36. Custom Context Manager
```python
import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start}")
```
**Explanation:** `__enter__` runs when the `with` block starts, `__exit__` runs when it ends.

### 37. Error Handling
```python
try:
    res = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
except TypeError:
    print("Wrong types")
```
**Explanation:** `try-except` blocks catch specific exceptions so the program doesn't crash.

### 38. Class Methods
```python
class Employee:
    @classmethod
    def from_string(cls, emp_str):
        name, pay = emp_str.split('-')
        return cls(name, int(pay))
```
**Explanation:** `@classmethod` receives the class (`cls`) as the first argument instead of an instance (`self`). Useful for alternative constructors.

### 39. Static Methods
```python
class Employee:
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5
```
**Explanation:** `@staticmethod` doesn't take `self` or `cls`. It's just a function that lives inside a class namespace.

### 40. Abstract Base Class
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```
**Explanation:** You cannot create an instance of an ABC. It forces subclasses to implement specific methods.

---

## Section 5: Professional Tools

### 41. Virtualenv Setup
1. `python -m venv venv` (Create)
2. `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. `pip install requests`
**Explanation:** Virtual environments isolate project dependencies to avoid version conflicts.

### 42. Logging System
```python
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info("App started")
```
**Explanation:** Logging is better than `print` because you can control levels (INFO, ERROR) and output locations (file, console).

### 43. Unit Testing
```python
import unittest
def is_valid(email): return "@" in email
class TestEmail(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid("test@me.com"))
```
**Explanation:** `unittest` provides a framework to verify that code works as expected automatically.

### 44. Subprocess Call
```python
import subprocess
result = subprocess.run(['ls'], capture_output=True, text=True)
print(result.stdout)
```
**Explanation:** `subprocess` lets you run terminal commands and get their results back into Python strings.

### 45. Environment Config
```python
import os
api_key = os.environ.get('API_KEY', 'default_secret')
```
**Explanation:** Storing secrets in environment variables instead of code is a security best practice.

### 46. SQLite Database
```python
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE students (name text, grade int)")
c.execute("INSERT INTO students VALUES ('Alice', 90)")
conn.commit()
```
**Explanation:** SQLite is a serverless database engine built into Python.

### 47. Matplotlib Plot
```python
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar']
expenses = [200, 150, 300]
plt.plot(months, expenses)
plt.show()
```
**Explanation:** `matplotlib` is the standard library for creating static, animated, and interactive visualizations.

### 48. Performance Profiling
```python
import timeit
print(timeit.timeit('[x for x in range(100)]', number=10000))
```
**Explanation:** `timeit` runs a code snippet thousands of times to give an accurate measurement of execution time.

### 49. CSV to JSON
```python
import csv, json
data = []
with open('data.csv') as f:
    for row in csv.DictReader(f):
        data.append(row)
with open('data.json', 'w') as f:
    json.dump(data, f)
```
**Explanation:** We read the CSV into a list of dictionaries, then use `json.dump` to write that list to a file.

### 50. Refactoring
**Explanation:** Refactoring involves improving code structure (e.g., adding functions, using descriptive names, removing global variables) without changing its external behavior.
