import pandas as pd
import numpy as np

# For getting the same random numbers every time
np.random.seed(42)

# Months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
]

# Generate random expenses

food = np.random.randint(2500, 4500, size=6)
books = np.random.randint(500, 1500, size=6)
rent = np.random.randint(6000, 7000, size=6)
travel = np.random.randint(800, 2000, size=6)

# Create DataFrame

df = pd.DataFrame({
    "Month": months,
    "Food": food,
    "Books": books,
    "Rent": rent,
    "Travel": travel
})

# Save to CSV

df.to_csv("student_expenses.csv", index=False)

print("CSV file created successfully!")
print(df)

import pandas as pd

# Read CSV file
df = pd.read_csv("student_expenses.csv")

print("Student Expense Data")
print(df)

# -------------------------------
# Total Expense
# -------------------------------

df["Total"] = df[["Food", "Books", "Rent", "Travel"]].sum(axis=1)

overall_total = df["Total"].sum()

print("\nTotal money spent in 6 months:")
print(overall_total)

# -------------------------------
# Highest Spending Category
# -------------------------------

category_totals = df[["Food", "Books", "Rent", "Travel"]].sum()

highest_category = category_totals.idxmax()

highest_amount = category_totals.max()

print("\nCategory with highest spending:")

print(highest_category)

print("Amount:", highest_amount)

# -------------------------------
# Predict Next Month Expense
# -------------------------------

rolling_average = df["Total"].rolling(window=3).mean()

prediction = rolling_average.iloc[-1]

print("\nPredicted next month's expense:")

print(round(prediction, 2))

df = pd.read_csv("student_expenses.csv") 