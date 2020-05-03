# Exercise_1 
# Create function that returns the average of an integer list
def average_numbers(num_list): 
    avg = sum(num_list)/float(len(num_list)) # divide by length of list
    return avg

# Take the average of a list: my_avg
my_avg = average_numbers([1, 2, 3, 4, 5, 6])

# Print out my_avg
print(my_avg)

--------------------------------------------------
# Exercise_2 
# Create a list that contains two lists: matrix
matrix = [[1,2,3,4], [5,6,7,8]]

# Print the matrix list
print(matrix)

--------------------------------------------------
# Exercise_3 
# Import numpy as np
import numpy as np

# List input: my_matrix
my_matrix = [[1,2,3,4], [5,6,7,8]] 

# Function that converts lists to arrays: return_array
def return_array(s):
    array = np.array(s, dtype = float)
    return array
    
# Call return_array on my_matrix, and print the output
print(return_array(my_matrix))

--------------------------------------------------
# Exercise_4 
# Create a class: DataShell
class DataShell: 
    pass

--------------------------------------------------
