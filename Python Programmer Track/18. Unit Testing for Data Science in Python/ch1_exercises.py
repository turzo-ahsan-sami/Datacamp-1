# Exercise_1 
#1
selected_option = 3
#2
selected_option = 1


--------------------------------------------------
# Exercise_2 
#1
# Import the pytest package
import pytest
#2
# Import the pytest package
import pytest

# Import convert_to_int() from the module preprocessing_helpers.py
from preprocessing_helpers import convert_to_int
#3
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  pass
#4
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081


--------------------------------------------------
# Exercise_3 
#1
selected_option = 2
#2
def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))


--------------------------------------------------
