# Exercise_1 
# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv(data_file)

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv(data_file, header=None)

# Print the output of df_headers.head()
print(df_headers.head())

--------------------------------------------------
# Exercise_2 
# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(",")

# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop, axis="columns")

# Print the output of df_dropped.head()
print(df_dropped.head())

--------------------------------------------------
# Exercise_3 
# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped["date"].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string = df_dropped["date"] + df_dropped["Time"]

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(df_clean.head())

--------------------------------------------------
# Exercise_4 
# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc["2011-06-20 08": "2011-06-20 09:00", "dry_bulb_faren"])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors="coerce")

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc["2011-06-20 08": "2011-06-20 09:00", "dry_bulb_faren"])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean["wind_speed"], errors="coerce")
df_clean['dew_point_faren'] = pd.to_numeric(df_clean["dew_point_faren"], errors="coerce")

--------------------------------------------------
# Exercise_5 
# Print the median of the dry_bulb_faren column
print(df_clean["dry_bulb_faren"].median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc["2011-Apr":"2011-Jun", 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc["2011-Jan", "dry_bulb_faren"].median())

--------------------------------------------------
# Exercise_6 
# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample("D").mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011["dry_bulb_faren"].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample("D").mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index()["Temperature"]

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())

--------------------------------------------------
# Exercise_7 
#1
# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean["sky_condition"] == "CLR"

# Filter df_clean using is_sky_clear
sunny = df_clean[is_sky_clear]

# Resample sunny by day then calculate the max
sunny_daily_max = sunny.resample("D").max()

# See the result
sunny_daily_max.head()
#2
# Using df_clean, when does sky_condition contain 'OVC'?
is_sky_overcast = df_clean["sky_condition"].str.contains("OVC")

# Filter df_clean using is_sky_overcast
overcast = df_clean[is_sky_overcast]

# Resample overcast by day then calculate the max
overcast_daily_max = overcast.resample("D").max()

# See the result
overcast_daily_max.head()
#3
# From previous steps
is_sky_clear = df_clean['sky_condition']=='CLR'
sunny = df_clean.loc[is_sky_clear]
sunny_daily_max = sunny.resample('D').max()
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')
overcast = df_clean.loc[is_sky_overcast]
overcast_daily_max = overcast.resample('D').max()

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()

# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()

# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean-overcast_daily_max_mean)


--------------------------------------------------
# Exercise_8 
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean[["visibility","dry_bulb_faren"]].resample("W").mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()

--------------------------------------------------
# Exercise_9 
#1
# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean["sky_condition"] == "CLR"

# Resample is_sky_clear by day
resampled = is_sky_clear.resample("D").sum()

# See the result
resampled
#2
# From previous step
is_sky_clear = df_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')

# Calculate the number of sunny hours per day
sunny_hours = resampled.sum()

# Calculate the number of measured hours per day
total_hours = resampled.count()

# Calculate the fraction of hours per day that were sunny
sunny_fraction = sunny_hours / total_hours
#3
# From previous steps
is_sky_clear = df_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')
sunny_hours = resampled.sum()
total_hours = resampled.count()
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind="box")
plt.show()


--------------------------------------------------
# Exercise_10 
# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean[["dew_point_faren", "dry_bulb_faren"]].resample("M").max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind="hist", bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()

--------------------------------------------------
# Exercise_11 
# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = df_climate.loc["2010-Aug","Temperature"].max()
print(august_max)

# Resample the August 2011 temperatures in df_clean by day and aggregate the maximum value: august_2011
august_2011 = df_clean.loc["2011-Aug","dry_bulb_faren"].resample("D").max()

# Filter out days in august_2011 where the value exceeded august_max: august_2011_high
august_2011_high = august_2011[august_2011 > august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(kind="hist", bins=25, normed=True, cumulative=True)

# Display the plot
plt.show()

--------------------------------------------------
