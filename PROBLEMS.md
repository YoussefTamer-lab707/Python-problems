# 50 Python Problem-Solving Challenges

Based on Corey Schafer's Python Tutorial Series.

## Section 1: Beginner Foundations (Difficulty: 1/5)
1.  **Greeting App:** Write a program that asks for a user's name and age, then prints a personalized greeting saying how many years they have until they turn 100.
2.  **String Reverser:** Create a function that takes a string and returns it reversed using slicing.
3.  **List Calculator:** Given a list of numbers, write a script to find the sum, average, and the largest number without using built-in `sum()` or `max()`.
4.  **Unique Elements:** Take a list with duplicate items and return a new list with only the unique elements using a Set.
5.  **Dictionary Lookup:** Create a dictionary of 5 countries and their capitals. Ask the user for a country and print its capital, handling cases where the country isn't found.
6.  **Case Swapper:** Write a program that takes a string and swaps the case of every letter (Upper to Lower and vice versa).
7.  **List Slicer:** Given a list of 10 numbers, print the first three, the last three, and the middle four elements using slicing.
8.  **Word Counter:** Ask the user for a sentence and count how many words it contains.
9.  **Type Checker:** Write a script that takes an input and identifies if it's an integer, float, or string.
10. **F-String Practice:** Create variables for a product name, price, and quantity. Use an f-string to print: "Item: [Name], Total: $[Price*Quantity]".

## Section 2: Control Flow & Functions (Difficulty: 2/5)
11. **Even/Odd Loop:** Iterate through numbers 1 to 20. Print "Even" for even numbers and "Odd" for odd numbers using an `if-else` block.
12. **FizzBuzz:** Print numbers 1 to 50. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for both, print "FizzBuzz".
13. **Prime Checker:** Write a function `is_prime(n)` that returns `True` if a number is prime and `False` otherwise.
14. **Args Summation:** Create a function `multiply_all(*args)` that takes any number of arguments and returns their product.
15. **Area Calculator:** Write a function that calculates the area of a circle or rectangle based on a keyword argument `shape`.
16. **LEGB Scope Demo:** Create a global variable and a function that tries to modify it. Use the `global` keyword and explain the difference.
17. **Lambda Filter:** Given a list of ages, use a `lambda` function with `filter()` to extract all ages over 18.
18. **Recursive Factorial:** Write a function to calculate the factorial of a number using recursion.
19. **Vowel Remover:** Write a function that takes a string and returns it with all vowels removed using a `for` loop.
20. **Dictionary Comprehension:** Given a list of numbers, create a dictionary where the key is the number and the value is its square, but only for even numbers.

## Section 3: Modules & Standard Library (Difficulty: 3/5)
21. **OS Explorer:** Use the `os` module to list all files in the current directory and print their sizes.
22. **Random Password:** Write a script using the `random` and `string` modules to generate a 12-character random password.
23. **Days Until Birthday:** Use the `datetime` module to calculate how many days are left until your next birthday.
24. **Permutation Generator:** Use `itertools.permutations` to find all possible arrangements of the letters in the word "CODE".
25. **JSON Parser:** Create a JSON string representing a person. Use the `json` module to load it into a dictionary and modify the "city" field.
26. **CSV Filter:** Create a CSV file with Names and Scores. Write a script to read it and print only people with scores above 80.
27. **Math Constants:** Write a script that uses the `math` module to calculate the area of a circle using `math.pi`.
28. **Zip & Map:** Given two lists (Names and Ages), use `zip()` to create a list of tuples, then use `map()` to convert ages to months (years * 12).
29. **Sys Arguments:** Write a script that accepts a name as a command-line argument using `sys.argv` and prints a greeting.
30. **Counter Tool:** Use `collections.Counter` to find the most common character in a long paragraph of text.

## Section 4: OOP & Advanced Features (Difficulty: 4/5)
31. **Employee Class:** Create an `Employee` class with attributes `name`, `email`, and `pay`. Add a method `apply_raise`.
32. **Inheritance (Developer):** Create a `Developer` subclass that inherits from `Employee` and adds a `prog_lang` attribute.
33. **Dunder Methods:** Implement `__str__` and `__repr__` for your `Employee` class to provide meaningful output.
34. **Property Decorators:** Add a `fullname` property to your class with a getter and setter that updates the first and last names.
35. **Generator expression:** Create a generator that yields the Fibonacci sequence up to a certain number to save memory.
36. **Custom Context Manager:** Write a class that can be used as a context manager (using `__enter__` and `__exit__`) to time how long a block of code takes to run.
37. **Error Handling:** Write a function that divides two numbers and uses `try-except` to handle `ZeroDivisionError` and `TypeError`.
38. **Class Methods:** Add a class method `from_string` to your `Employee` class that allows creating an instance from a string like "John-Doe-70000".
39. **Static Methods:** Add a static method `is_workday` that takes a date and returns whether it's a weekday.
40. **Abstract Base Class:** Use the `abc` module to create an abstract `Shape` class with an abstract `area` method.

## Section 5: Professional Tools & Best Practices (Difficulty: 5/5)
41. **Virtualenv Setup:** Write a step-by-step README on how to create a virtual environment, activate it, and install `requests`.
42. **Logging System:** Implement a script that logs "Info", "Warning", and "Error" messages to a file named `app.log` instead of printing them.
43. **Unit Testing:** Write a `unittest` script for a function that validates if an email address is properly formatted.
44. **Subprocess Call:** Use the `subprocess` module to run the `ls` (or `dir`) command and capture the output into a Python variable.
45. **Environment Config:** Use `os.environ` to read a secret API Key from an environment variable and provide a fallback if it doesn't exist.
46. **SQLite Database:** Create a small database `students.db`, create a table, insert 3 records, and query them.
47. **Matplotlib Plot:** Write a script to plot a simple line graph of "Monthly Expenses" over 6 months using `matplotlib`.
48. **Performance Profiling:** Use the `timeit` module to compare the performance of a List Comprehension vs. a standard `for` loop.
49. **CSV to JSON:** Write a script that reads a CSV file and converts every row into a JSON object, saving the final list to a `.json` file.
50. **Refactoring:** Take a "messy" script (provided in your head) and refactor it to use functions, proper naming conventions, and docstrings.
