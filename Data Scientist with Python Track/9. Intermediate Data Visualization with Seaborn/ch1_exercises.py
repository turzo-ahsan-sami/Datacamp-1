# Exercise_1 
# import all modules
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv(grant_file)

--------------------------------------------------
# Exercise_2 
#1
# Display pandas histogram
df['Award_Amount'].plot.hist();
plt.show()

# Clear out the pandas histogram
plt.clf()
#2
# Display a Seaborn distplot
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()


--------------------------------------------------
# Exercise_3 
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()

--------------------------------------------------
# Exercise_4 
# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()

--------------------------------------------------
# Exercise_5 
#1
sns.regplot(data=df,
         x="insurance_losses",
         y="premiums")
plt.show()
#2
sns.lmplot(data=df,
         x="insurance_losses",
         y="premiums")
plt.show()


--------------------------------------------------
# Exercise_6 
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()

--------------------------------------------------
# Exercise_7 
# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()

--------------------------------------------------
