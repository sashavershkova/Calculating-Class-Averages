import pytest
from main import calculate_class_averages
# Test cases
def test_class_averages_for_multiple_students_and_classes():
    school_scores = {
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

    expected = {
        "Math": 88.17,
        "Science": 85.67,
        "History": 81.5
    }

    result = calculate_class_averages(school_scores)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_class_with_no_students_should_return_zero_average():
    school_scores = {
        "Math": {},
        "Science": {
            "Alice": [80, 85, 88],
            "Bob": [78, 82, 85]
        }
    }

    expected = {
        "Math": 0,
        "Science": 83.0
    }

    result = calculate_class_averages(school_scores)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_single_student_single_class():
    school_scores = {
        "Math": {
            "Alice": [100, 95, 98]
        }
    }

    expected = {
        "Math": 97.67
    }

    result = calculate_class_averages(school_scores)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_class_with_all_empty_score_lists_should_return_zero_average():
    school_scores = {
        "Math": {
            "Alice": [],
            "Bob": []
        }
    }

    expected = {
        "Math": 0
    }

    result = calculate_class_averages(school_scores)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_mixed_scores_across_students_and_classes():
    school_scores = {
        "Math": {
            "Alice": [85, 90, 78],
            "Bob": [70, 80, 90]
        },
        "English": {
            "Charlie": [100, 90, 85],
            "Diana": [95, 85]
        }
    }

    expected = {
        "Math": 82.17,
        "English": 91.0
    }

    result = calculate_class_averages(school_scores)
    assert result == expected, f"Expected {expected}, but got {result}"
