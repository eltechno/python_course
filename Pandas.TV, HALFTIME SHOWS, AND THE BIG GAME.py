# Import pandas
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
#%matplotlib inline

# Load the CSV data into DataFrames
super_bowls = pd.read_csv('super_bowls.csv')
tv = pd.read_csv("tv.csv")
halftime_musicians = pd.read_csv('halftime_musicians.csv')

# Display the first five rows of each DataFrame
print (super_bowls.head())
print (tv.head())
print (halftime_musicians.head())


# Summary of the TV data to inspect
tv.info()

print('\n')

# Summary of the halftime musician data to inspect
halftime_musicians.info()


# Import matplotlib and set plotting style

plt.style.use('seaborn')

# Plot a histogram of combined points
# ... YOUR CODE FOR TASK 3 ...

plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls['combined_pts'] > 70])
print(super_bowls[super_bowls['combined_pts'] < 25])

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
#Select the Super Bowl(s) where the point difference was equal to 1.
print(super_bowls[super_bowls['difference_pts'] == 1])
#Select the Super Bowl(s) where the point difference was greater than or equal to 35.
print(super_bowls[super_bowls['difference_pts'] <= 35])

#We can plot household share (average percentage of U.S. households with a TV in use that
# were watching for the entire broadcast) vs. point difference to find out.

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')
#merge (pd. left, pd right, on=LABEL)


# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)
