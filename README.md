# Python Regex Compilation and Searching 🔎

A simple Python program demonstrating how to use **Regular Expressions** with `re.compile()`, `re.findall()`, and `re.finditer()`.

## 📌 Description

This program searches for **10-digit phone numbers** from:

1. A string containing phone numbers.
2. A text file named `student_details`.

It demonstrates how compiling a regex pattern can be useful when the same pattern needs to be used multiple times.

## 💻 Code

```python
import re

phones = "John-8956237845, Carol-7845128956, mark-0123456578"

pattern = r"\d{10}"

# Compile the regex pattern
pattern_compiled = re.compile(pattern)

print(pattern_compiled)
print(type(pattern_compiled))

# Find all phone numbers
match_obj = re.findall(pattern_compiled, phones)

print(match_obj)


# Read student details from a file
with open("student_details", "r") as fh:
    data = fh.read()

print(data)


# Find all matches using finditer()
phone_matches = re.finditer(pattern_compiled, data)

print(phone_matches)

for match in phone_matches:
    print(match)
```

## 🖥️ Example Output

For the string:

```text
John-8956237845, Carol-7845128956, mark-0123456578
```

The output from `findall()` will be:

```text
['8956237845', '7845128956', '0123456578']
```

`finditer()` returns an iterator containing match objects.

Example:

```text
<re.Match object; span=(...), match='8956237845'>
<re.Match object; span=(...), match='7845128956'>
```

The exact `span` values depend on the contents of the `student_details` file.

## 🧠 Key Concepts

### 1. `\d{10}`

```python
pattern = r"\d{10}"
```

This pattern matches exactly **10 digits**.

* `\d` → any digit from 0 to 9
* `{10}` → exactly 10 repetitions

### 2. `re.compile()`

```python
pattern_compiled = re.compile(pattern)
```

Compiles the regex pattern into a reusable **Pattern object**.

This is useful when the same pattern is used multiple times.

### 3. `re.findall()`

```python
re.findall(pattern_compiled, phones)
```

Returns **all matching values as a list**.

Example:

```text
['8956237845', '7845128956', '0123456578']
```

### 4. `re.finditer()`

```python
re.finditer(pattern_compiled, data)
```

Returns an iterator containing **match objects**.

Each match object contains information such as:

* Matched text
* Starting position
* Ending position

You can access the matched text using:

```python
match.group()
```

And its position using:

```python
match.span()
```

## 📁 Project Structure

```text
project/
│
├── regex_example.py
├── student_details
└── README.md
```

The `student_details` file should contain student information with phone numbers for `finditer()` to search.

## 🛠️ Technologies Used

* Python 3
* `re` module
* File Handling

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Create a file named `student_details`.
3. Add some text containing 10-digit phone numbers.
4. Save the Python code as `regex_example.py`.
5. Run:

```bash
python regex_example.py
```

## 📚 Learning Outcome

This example helps understand:

* Regular Expressions
* `re.compile()`
* `re.findall()`
* `re.finditer()`
* Match objects
* `group()`
* `span()`
* Reading files using Python

## 👨‍💻 Author

**Kotapati Dhananjay**
