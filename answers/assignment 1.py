import polars as pl

# Load data from CSV
df = pl.read_csv("../dummy_data.csv")
print(df)

# Select specific columns
df_selected = df.select(["Name", "Age", "City"])
print(df_selected)

# Filter rows where Age is greater than 30
df_filtered = df.filter(pl.col("Age") > 30)
print(df_filtered)

# Add a new column 'Bonus' which is 10% of 'Salary'
df = df_filtered.with_columns((pl.col("Salary") * 0.1).alias("Bonus"))
print(df)

# Group by 'Department' and calculate average 'Salary'
df_grouped = df.group_by("Department").agg(pl.col("Salary").mean().alias("Average Salary"))
print(df_grouped)
df_grouped.write_csv("../grouped_data.csv")
