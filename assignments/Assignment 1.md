
# Assignment: Data Analysis and Plotting with Polars and Matplotlib

## Objective:
The goal of this assignment is to help you understand how to perform basic data manipulation with the `Polars` library and create visualizations using `Matplotlib` in Python. You will load data, group it, perform aggregations, and visualize the results.

---

## Instructions:
Follow the steps below to complete the assignment. Each step corresponds to a specific task involving data manipulation and plotting.

---

## Step 1: Importing Libraries
1. Import the required libraries: `Polars` for data manipulation and `Matplotlib` for plotting.

**Code Snippet to Start With:**
```python
import polars as pl
import matplotlib.pyplot as plt
```

---

## Step 2: Loading Data
1. Load data from a CSV file located at `"../dummy_data.csv"` into a Polars DataFrame.
2. Print the loaded DataFrame.

**Hint:** Use the `pl.read_csv()` function.

---

## Step 3: Grouping and Aggregating Data
1. Group the data by the `"Age"` column.
2. Calculate the average `"Salary"` for each age group and save it as `"Average Salary"`.
3. Sort the grouped data by `"Age"`.

**Code Snippet:**
```python
df_avg_income_per_age = (
    df.group_by("Age")
    .agg(pl.col("Salary").mean().alias("Average Salary"))
    .sort("Age")
)
```

---

## Step 4: Plotting the Data
1. Create a plot to visualize the average income per age group.
2. Plot `"Age"` on the x-axis and `"Average Salary"` on the y-axis.
3. Add appropriate labels, title, and grid to the plot.

**Code Snippet:**
```python
# Plot: Average Income per Age directly from Polars columns
plt.figure(figsize=(10, 6))
plt.plot(df_avg_income_per_age["Age"], df_avg_income_per_age["Average Salary"], marker='o', linestyle='-', color='teal')
plt.title("Average Income per Age")
plt.xlabel("Age")
plt.ylabel("Average Salary")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## Sample Output (for Reference):

1. **DataFrame (Step 2):**
```
┌─────┬───────────┐
│ Age │ Salary    │
├─────┼───────────┤
│ 28  │ 50000     │
│ 34  │ 60000     │
│ ... │ ...       │
```

2. **Grouped Data (Step 3):**
```
┌─────┬────────────────┐
│ Age │ Average Salary │
├─────┼────────────────┤
│ 25  │ 45000          │
│ 30  │ 55000          │
│ ... │ ...            │
```

3. **Plot (Step 4):**
   The plot should show a line graph with "Age" on the x-axis and "Average Salary" on the y-axis, illustrating how salary changes with age.
