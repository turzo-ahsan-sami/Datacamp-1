# Exercise_1 
#1
# Compute the PMF for year
pmf_year = Pmf(gss['year'],normalize=False)

# Print the result
print(pmf_year)
#2
selected_option = 1


--------------------------------------------------
# Exercise_2 
#1
# Select the age column
age = gss['age']
#2
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)
#3
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

# Plot the PMF
pmf_age.bar()

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()


--------------------------------------------------
# Exercise_3 
#1
# Select the age column
age = gss['age']
#2
# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)
#3
# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
print(cdf_age[30])
#4
selected_option = 1


--------------------------------------------------
# Exercise_4 
#1
# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)
#2
# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)
#3
# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)
#4
selected_option = 1


--------------------------------------------------
# Exercise_5 
# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()

--------------------------------------------------
# Exercise_6 
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = gss[bach & gss['year'] >= 14]

# High school (12 or fewer years of education)
high = educ <= 12
print(high.mean())

--------------------------------------------------
# Exercise_7 
income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()

--------------------------------------------------
# Exercise_8 
# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(gss['realinc'])

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print(mean, std)

# Make a norm object
from scipy.stats import norm
dist = norm(0, 1)

--------------------------------------------------
# Exercise_9 
# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()

--------------------------------------------------
# Exercise_10 
# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()

--------------------------------------------------
