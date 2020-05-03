# Exercise_1 
# Import the package with a name that follows PEP 8
import text_analyzer


--------------------------------------------------
# Exercise_2 
# Import local packages
import package
import py_package

# View the help for each package
help(py_package)
help(package)


--------------------------------------------------
# Exercise_3 
#1
# Import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)

#2
# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())

#3
selected_option = 2


--------------------------------------------------
# Exercise_4 
# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)


--------------------------------------------------
# Exercise_5 
requirements = """
matplotlib>=3.0.0
numpy==1.15.4
pandas<=0.22.0
pycodestyle
"""

--------------------------------------------------
# Exercise_6 
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='dd',
      packages=['text_analyzer'])


--------------------------------------------------
# Exercise_7 
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='ddd',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])


--------------------------------------------------
