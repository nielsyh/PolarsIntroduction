import polars as pl
import matplotlib.pyplot as plt

# Load data from CSV
df = pl.read_csv("../dummy_data.csv")

# Group by 'Age' and calculate average 'Salary', then sort by 'Age'
df_avg_income_per_age = (
    df.group_by("Age")
    .agg(pl.col("Salary").mean().alias("Average Salary"))
    .sort("Age")
)

# Plot: Average Income per Age directly from Polars columns
plt.figure(figsize=(10, 6))
plt.plot(df_avg_income_per_age["Age"], df_avg_income_per_age["Average Salary"], marker='o', linestyle='-', color='teal')
plt.title("Average Income per Age")
plt.xlabel("Age")
plt.ylabel("Average Salary")
plt.grid(True)
plt.tight_layout()
plt.show()
