# Exercise_1 
# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone['x'], cellphone['y'])

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

--------------------------------------------------
# Exercise_2 
#1
# Change the marker color to red
plt.scatter(cellphone.x, cellphone.y,
           color='red')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
#2
# Change the marker shape to square
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
#3
# Change the transparency to 0.1
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha=0.1)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()


--------------------------------------------------
# Exercise_3 
#1
# Display the DataFrame hours using print
print(hours)
#2
# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar( hours.officer,hours.avg_hours_worked)

# Display the plot
plt.show()
#3
# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked,
        # Add error bars
        yerr=hours.std_hours_worked)

# Display the plot
plt.show()


--------------------------------------------------
# Exercise_4 
#1
# Plot the number of hours spent on desk work
plt.bar(hours.officer,hours.desk_work,label='Desk Work')

# Display the plot
plt.show()
#2
# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer,hours.field_work,label='Field Work',bottom=hours.desk_work)

# Add a legend
plt.legend()

# Display the plot
plt.show()


--------------------------------------------------
# Exercise_5 
#1
# Create a histogram of the column weight
# from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
#2
# Change the number of bins to 50
plt.hist(puppies.weight,
        bins=50)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
#3
# Change the range to start at 5 and end at 35
plt.hist(puppies.weight,
        range=(5, 35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()


--------------------------------------------------
# Exercise_6 
#1
# Create a histogram of gravel.radius
plt.hist(gravel.radius)

# Display histogram
plt.show()
#2
# Create a histogram
# Range is 2 to 8, with 40 bins
plt.hist(gravel.radius, bins=40, range=(2,8))

# Display histogram
plt.show()
#3
# Create a histogram
# Normalize to 1
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Display histogram
plt.show()
#4
# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()


--------------------------------------------------
