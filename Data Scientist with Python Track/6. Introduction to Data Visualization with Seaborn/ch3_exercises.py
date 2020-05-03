# Exercise_1 
#1
# Create count plot of internet usage
sns.catplot(x="Internet usage",
data=survey_data,
kind="count")

# Show plot
plt.show()
#2
# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()
#3
# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",col='Age Category')

# Show plot
plt.show()


--------------------------------------------------
# Exercise_2 
# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender",
y="Interested in Math",
data=survey_data,
kind="bar")


# Show plot
plt.show()

--------------------------------------------------
# Exercise_3 
#1
# Create bar plot of average final grade in each study category
sns.catplot(x="study_time",
y="G3",
data=student_data,
kind="bar")


# Show plot
plt.show()
#2
# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"])

# Show plot
plt.show()
#3
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],ci=None)

# Show plot
plt.show()


--------------------------------------------------
# Exercise_4 
#1
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
g = sns.catplot(x="study_time",
y="G3",
data=student_data,
order=study_time_order,
kind="box")




# Show plot
plt.show()
#2
selected_option = 4


--------------------------------------------------
# Exercise_5 
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet",
y="G3",
data=student_data,
kind="box",
hue='location',sym='')





# Show plot
plt.show()

--------------------------------------------------
# Exercise_6 
#1
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",whis=0.5)

# Show plot
plt.show()
#2
# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()
#3
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()


--------------------------------------------------
# Exercise_7 
#1
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel",
y="absences",
data=student_data,
kind="point")


            
# Show plot
plt.show()
#2
# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",capsize=0.2)
        
# Show plot
plt.show()
#3
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,join=False)
            
# Show plot
plt.show()


--------------------------------------------------
# Exercise_8 
#1
# Create a point plot with subgroups
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",hue='school')


# Show plot
plt.show()
#2
# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",ci=None)

# Show plot
plt.show()
#3
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",estimator=median,
            ci=None)

# Show plot
plt.show()


--------------------------------------------------
