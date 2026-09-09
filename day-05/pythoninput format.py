# Python Input Formatting 
## Introduction

In Python, input is taken using the `input()` function. By default, all user input is treated as a **string**, so type conversion is required when working with numbers or other data types.

---

## 1. input() Function

* Used to take input from the user
* Always returns data in **string format**

```python
x = input()
print(type(x))  # str
```

### Theory:

* Even if you enter numbers, Python stores them as text
* Example: entering `10` → stored as `"10"`

---

## 2. Type Conversion

To use input as numbers, we convert it using built-in functions:

### Integer Conversion

```python
x = int(input())
```

### Float Conversion

```python
x = float(input())
```

### Theory:

* Type casting converts one data type to another
* Required for performing mathematical operations

---

## 3. Multiple Inputs using split()

* `split()` divides input into multiple values based on spaces

```python
names = input().split()
```

### Example:

Input: `usha dumkuu`
Output: `['usha', 'dumkuu']`

### Theory:

* Returns a **list of strings**
* Default separator is space
* Can also specify separators like `split(",")`

---

## 4. Tuple Input

```python
names = tuple(input().split())
```

### Theory:

* Converts list into **tuple**
* Tuples are immutable (cannot be changed)

---

## 5. Map Function

* Used to apply a function to all elements in an iterable
* Syntax: `map(function, iterable)`

```python
marks = list(map(int, input().split()))
```

### Theory:

* Converts each element from string to integer
* Efficient way to handle multiple inputs
* Returns a **map object**, so we convert it into list/tuple/set

---

## 6. Data Structures with map()

### List

```python
marks = list(map(int, input().split()))
```

### Tuple

```python
marks = tuple(map(int, input().split()))
```

### Set

```python
marks = set(map(int, input().split()))
```

### Float List

```python
marks = list(map(float, input().split()))
```

### Theory:

* **List** → ordered, mutable
* **Tuple** → ordered, immutable
* **Set** → unordered, no duplicates

---

## 7. eval() Function

* Evaluates input as a Python expression

```python
x = eval(input())
```

### Examples:

#### Integer

Input: `10` → Output: `10`

#### List

Input: `[1, 2, 3]` → Output: `[1, 2, 3]`

#### Expression

Input: `5 + 3 * 2` → Output: `11`

### Theory:

* Automatically detects data type
* Can evaluate expressions and data structures

---

##  Disadvantages of eval()

* **Security Risk**: Can execute harmful code
* Should not be used with untrusted input

---

## Key Differences

| Feature | input()     | map()                    | eval()                |
| ------- | ----------- | ------------------------ | --------------------- |
| Type    | String      | Converts multiple values | Auto-detects          |
| Safety  | Safe        | Safe                     | Risky                 |
| Usage   | Basic input | Bulk conversion          | Expression evaluation |

---

## Final Summary

* `input()` → takes string input
* `int()`, `float()` → convert data types
* `split()` → multiple inputs
* `map()` → convert multiple values efficiently
* `list()`, `tuple()`, `set()` → store data
* `eval()` → powerful but risky function