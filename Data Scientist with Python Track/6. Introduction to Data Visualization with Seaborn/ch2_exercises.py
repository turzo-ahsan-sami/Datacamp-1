# Exercise_1 
#1
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data,kind="scatter")

# Show plot
plt.show()
#2
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",col="study_time")

# Show plot
plt.show()
#3
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()


--------------------------------------------------
# Exercise_2 
#1
# Create a scatter plot of G1 vs. G3
sns.relplot(x="G1",
y="G3",
data=student_data,
kind="scatter")



# Show plot
plt.show()
#2
# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter",col='schoolsup',
col_order=["yes",'no'])

# Show plot
plt.show()
#3
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row='famsup',
            row_order=["yes", "no"])

# Show plot
plt.show()


--------------------------------------------------
# Exercise_3 
#1
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower",
y="mpg",
data=mpg,
kind="scatter",
size="cylinders")



# Show plot
plt.show()
#2
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",hue='cylinders')

# Show plot
plt.show()


--------------------------------------------------
# Exercise_4 
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin",hue='origin')



# Show plot
plt.show()

--------------------------------------------------
# Exercise_5 
#1
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x="model_year", y="mpg",
data=mpg,
kind="line")


# Show plot
plt.show()
#2
selected_option = 2


--------------------------------------------------
# Exercise_6 
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci="sd")

# Show plot
plt.show()

--------------------------------------------------
# Exercise_7 
#1
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower",
data=mpg,
kind="line",
ci=None)



# Show plot
plt.show()
#2
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None,style='origin')

# Show plot
plt.show()
#3
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",dashes=True)

# Show plot
plt.show()


--------------------------------------------------
