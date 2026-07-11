# Day 09 - Dictionaries in Python

**Date:** 11-07-2026

---

# What I learned today

Today I learned about **Dictionaries** in Python. A dictionary stores data in **key-value pairs** and is mutable, meaning its contents can be changed after creation.

I also learned how to:

- Create a dictionary
- Access values using keys
- Add new key-value pairs
- Update existing values
- Delete keys
- Loop through dictionaries
- Use nested dictionaries
- Build a Contact Book project using dictionaries

---

# Syntax

## Create a Dictionary

```python
student = {
    "name": "Pratik",
    "age": 20,
    "branch": "CSE"
}
```

---

## Access Values

```python
print(student["name"])
print(student["age"])
```

---

## Add New Data

```python
student["college"] = "ABC University"
```

---

## Update Data

```python
student["age"] = 21
```

---

## Delete Data

```python
del student["branch"]
```

---

## Loop Through Dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

## Useful Dictionary Methods

```python
student.keys()

student.values()

student.items()

student.get("name")
```

---

# Mini Project

## Contact Book

Features:

- View All Contacts
- Add Contact
- Update Contact
- Delete Contact
- Search Contact
- Exit

Example Structure

```python
contacts = {
    "John": {
        "phone": "9876543210",
        "email": "john@gmail.com"
    }
}
```

---

# Commands I used today

```bash
python practice.py

python contact_book.py

git add .

git commit -m "Day 09: Learned dictionaries and built Contact Book"

git push
```

---

# One new thing I discovered

A dictionary stores data using **keys instead of indexes**, making searching and updating data much faster than lists.

---

# Interview Questions

### 1. What is a dictionary?

A mutable collection of key-value pairs.

---

### 2. Difference between List and Dictionary?

List uses indexes.

Dictionary uses keys.

---

### 3. How do you add a new key?

```python
student["city"] = "Nagpur"
```

---

### 4. How do you update a value?

```python
student["age"] = 21
```

---

### 5. How do you delete a key?

```python
del student["age"]
```

---

### 6. What does `keys()` return?

Returns all keys in the dictionary.

---

### 7. What does `values()` return?

Returns all values.

---

### 8. What does `items()` return?

Returns all key-value pairs.

---

### 9. What is `get()`?

Safely retrieves a value without raising an error if the key is missing.

---

### 10. Can dictionaries have duplicate keys?

No. Keys must be unique.

---

# Today's Achievement

✅ Learned Dictionaries

✅ Practiced Dictionary CRUD

✅ Learned Nested Dictionaries

✅ Built Contact Book Project

✅ Revised Git Workflow

---

# Progress Tracker

Day 01 ✅

Day 02 ✅

Day 03 ✅

Day 04 ✅

Day 05 ✅

Day 06 ✅

Day 07 ✅

Day 08 ✅

Day 09 ✅