# Exercise_1 
# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())

--------------------------------------------------
# Exercise_2 
#1
#Use .info() to inspect the DataFrame credit_records
print(credit_records.info())
#2
selected_option = 2


--------------------------------------------------
# Exercise_3 
#1
# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)
#2
# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)


--------------------------------------------------
# Exercise_4 
# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)

--------------------------------------------------
# Exercise_5 
#1
# Use info() to inspect mpr
print(mpr.info())
#2
# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr['Dog Name']

# Select column "Missing?" from mpr
is_missing = mpr['Missing?']

# Display the columns
print(name)
print(is_missing)
#3
selected_option = 3


--------------------------------------------------
# Exercise_6 
#1
# Is height_inches greater than 70 inches?
print(height_inches > 70)
#2
# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")
#3
# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")


--------------------------------------------------
# Exercise_7 
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)

--------------------------------------------------
# Exercise_8 
#1
# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)
#2
selected_option = 3


--------------------------------------------------
