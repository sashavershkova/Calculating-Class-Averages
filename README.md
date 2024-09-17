# Calculating Class Averages

## Problem Statement
Write a function called `calculate_class_averages` that takes a dictionary, `classrooms`, containing student exam scores for different classes. Your function should return a new dictionary where the keys are class names and the values are the average exam scores for that class. After implementing your function, use `pytest` to see if you pass the all the tests. If a classroom has 0 students in it then it should return 0.

## Example Input
```python
{
    "Math": {
        "Alice": [85, 90, 78],
        "Bob": [72, 88, 91],
        "Charlie": [95, 100, 92]
    },
    "Science": {
        "Alice": [80, 85, 88],
        "Bob": [78, 82, 85],
        "Diana": [90, 91, 89]
    },
    "History": {
        "Charlie": [70, 75, 80],
        "Diana": [88, 92, 84]
    }
}
```

## Example Output
```python
{
    "Math": 88.17,
    "Science": 85.67,
    "History": 81.5
}
```
## Example Input
```python
{
    "Math": {},
    "Science": {
        "Alice": [80, 85, 88],
        "Bob": [78, 82, 85]
    }
}
```
## Example Output
```python
{
    "Math": 0,
    "Science": 83.0
}
```