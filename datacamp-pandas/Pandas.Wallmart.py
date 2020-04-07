import pandas as pd
import numpy as np

sales = pd.read_pickle("walmart_sales.pkl.bz2", compression="bz2")

# Print the head of the sales DataFrame
print(sales.head())
# Print the info about the sales DataFrame
print(sales.info())
# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())
# Print the median of weekly_sales
print(sales["weekly_sales"].median())
# Print the maximum of the date column
print(sales["date"].max())
# Print the minimum of the date column
print(sales["date"].min())

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c","fuel_price_usd_per_l","unemployment"]].agg(iqr))

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))



# Sort sales by date
sales = sales.sort_values("date",ascending=[True])
# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales["cum_weekly_sales"] = sales["weekly_sales"].cumsum()
# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales["cum_max_sales"] = sales["weekly_sales"].cummax()
# See the columns you calculated
print(sales[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
print(sales.columns)


# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())
# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())
# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")
# Print date col of holiday_dates
print(holiday_dates["date"])

print(store_depts.columns)
print(store_types.columns)

# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["store"].value_counts(normalize="True")
print(store_props)

# Count the number of departments of each type and sort
dept_counts_sorted = store_depts["type"].value_counts(sort="True")
print(dept_counts_sorted)

# Get the proportion of departments of each type and sort
dept_props_sorted = store_depts["type"].value_counts(sort="True", normalize="True")
print(dept_props_sorted)




# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()
# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)


# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)


# From previous step
sales_by_type = sales.groupby('type')["is_holiday"].sum()
# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)




# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])
# Print sales_stats
print(sales_stats)
# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])
# Print unemp_fuel_stats
print(unemp_fuel_stats)

#pivot tables
# dogs.groupby("color")["weight_kg"].mean
# dogs.pivot_table(value="weight_kg", index="color)
# in the pivot table choose value as the column to sumarize
# and index as the columns to sumarize
# by default pivot table use the mean value
#
# to use another function
# dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median)
# to use mutiple funcs pass a list [np.media, np.mean]
#
# pivot with two variables
# dogs.groupby(["color", "breed"])["weight_kg"].mean()
#
# dogs.pivot_table(values="weight_kg", index="color", columns="breed")
# dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0)
# dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0, margins=True)


# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")
# Print mean_sales_by_type
print(mean_sales_by_type)
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean,np.median])
# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")
# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value="0"))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value="0", margins="True"))