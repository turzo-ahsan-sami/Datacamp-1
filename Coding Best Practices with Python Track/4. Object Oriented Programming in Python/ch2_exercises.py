# Exercise_1 
# Create empty class: DataShell
class DataShell:
  
    # Pass statement
    pass

# Instantiate DataShell: my_data_shell
my_data_shell = DataShell()

# Print my_data_shell
print(my_data_shell)

--------------------------------------------------
# Exercise_2 
# Create class: DataShell
class DataShell:
  
	# Initialize class with self argument
    def __init__(self):
      
        # Pass statement
        pass

# Instantiate DataShell: my_data_shell
my_data_shell = DataShell()

# Print my_data_shell
print(my_data_shell)

--------------------------------------------------
# Exercise_3 
# Create class: DataShell
class DataShell:
  
	# Initialize class with self and integerInput arguments
    def __init__(self, integerInput):
      
		# Set data as instance variable, and assign the value of integerInput
        self.data = integerInput

# Declare variable x with value of 10
x = 10

# Instantiate DataShell passing x as argument: my_data_shell
my_data_shell = DataShell(x)

# Print my_data_shell
print(my_data_shell.data)

--------------------------------------------------
# Exercise_4 
# Create class: DataShell
class DataShell:
  
	# Initialize class with self, identifier and data arguments
    def __init__(self, identifier, data):
      
		# Set identifier and data as instance variables, assigning value of input arguments
        self.identifier = identifier
        self.data = data

# Declare variable x with value of 100, and y with list of integers from 1 to 5
x = 100
y = [1, 2, 3, 4, 5]

# Instantiate DataShell passing x and y as arguments: my_data_shell
my_data_shell = DataShell(x, y)

# Print my_data_shell.identifier
print(my_data_shell.identifier)

# Print my_data_shell.data
print(my_data_shell.data)

--------------------------------------------------
# Exercise_5 
# Create class: DataShell
class DataShell:
  
    # Declare a class variable family, and assign value of "DataShell"
    family = "DataShell"
    
    # Initialize class with self, identifier arguments
    def __init__(self, identifier):
      
        # Set identifier as instance variable of input argument
        self.identifier = identifier

# Declare variable x with value of 100
x = 100

# Instantiate DataShell passing x as argument: my_data_shell
my_data_shell = DataShell(x)

# Print my_data_shell class variable family
print(my_data_shell.family)

--------------------------------------------------
# Exercise_6 
# Create class: DataShell
class DataShell:
  
    # Declare a class variable family, and assign value of "DataShell"
    family = "DataShell"
    
    # Initialize class with self, identifier arguments
    def __init__(self, identifier):
      
        # Set identifier as instance variables, assigning value of input arguments
        self.identifier = identifier

# Declare variable x with value of 100
x = 100

# Instantiate DataShell passing x as the argument: my_data_shell
my_data_shell = DataShell(x)

# Print my_data_shell class variable family
print(my_data_shell.family)

# Override the my_data_shell.family value with "NotDataShell"
my_data_shell.family = 'NotDataShell'

# Print my_data_shell class variable family once again
print(my_data_shell.family)

--------------------------------------------------
# Exercise_7 
# Create class: DataShell
class DataShell:
  
	# Initialize class with self argument
    def __init__(self):
        pass
      
	# Define class method which takes self argument: print_static
    def print_static(self):
        # Print string
        print("You just executed a class method!")
        
# Instantiate DataShell taking no arguments: my_data_shell
my_data_shell = DataShell()

# Call the print_static method of your newly created object
my_data_shell.print_static()

--------------------------------------------------
# Exercise_8 
# Create class: DataShell
class DataShell:
  
	# Initialize class with self and dataList as arguments
    def __init__(self, dataList):
      	# Set data as instance variable, and assign it the value of dataList
        self.data = dataList
        
	# Define class method which takes self argument: show
    def show(self):
        # Print the instance variable data
        print(self.data)

# Declare variable with list of integers from 1 to 10: integer_list   
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
# Instantiate DataShell taking integer_list as argument: my_data_shell
my_data_shell = DataShell(integer_list)

# Call the show method of your newly created object
my_data_shell.show()

--------------------------------------------------
# Exercise_9 
# Create class: DataShell
class DataShell:
  
	# Initialize class with self and dataList as arguments
    def __init__(self, dataList):
      	# Set data as instance variable, and assign it the value of dataList
        self.data = dataList
        
	# Define method that prints data: show
    def show(self):
        print(self.data)
        
    # Define method that prints average of data: avg 
    def avg(self):
        # Declare avg and assign it the average of data
        avg = sum(self.data)/float(len(self.data))
        # Print avg
        print(avg)
        
# Instantiate DataShell taking integer_list as argument: my_data_shell
my_data_shell = DataShell(integer_list)

# Call the show and avg methods of your newly created object
my_data_shell.show()
my_data_shell.avg()

--------------------------------------------------
