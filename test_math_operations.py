import unittest
from math_operations import add, subtract, calculate_range


# assert is a keyword in Python that is commonly used in unit tests
# to check if a given condition is true. If the condition is true,
# the program continues to execute normally. If the condition is false,
# assert will raise an AssertionError and the program will stop running.

def test_add():
    assert add(2,3) == 5
    assert add(5,5) == 10
    assert add(10,10) == 20

def test_subtract():
    assert subtract(5,5) == 0
    assert subtract(8,5) == 3

def test_add_with_none():
    assert add(None, 5) is None
    assert add(6, None) is None

def test_subtract_with_none():
    assert subtract(5, None) is None
    assert subtract(None, 1) is None

def test_add_with_string():
    assert add("hello", "world") == "helloworld"

import pandas as pd
def assert_df_equality(df_output, df_expected):
    pd.testing.assert_frame_equal(df_output, df_expected)

def test_calculate_range():
    input_data = {
        "open": [0.536353, 0.552352],
        "high": [0.553633, 0.753566],
        "low": [0.363643, 0.636466],
        "close": [0.35352, 0.252353]
    }

    df_input = pd.DataFrame(input_data)

    expected_output = {
        "open": [0.536353, 0.552352],
        "high": [0.553633, 0.753566],
        "low": [0.363643, 0.636466],
        "close": [0.35352, 0.252353],
        "range": [0.18999, 0.1171] # high - low
    }
    df_expected = pd.DataFrame(expected_output)

    # call function
    df_output = calculate_range(df_input)

    # Assert that the output DataFrame matches the expected DataFrame
    assert_df_equality(df_output, df_expected)