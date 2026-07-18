import pandas as pd

# Load the dataset you just generated
# (Make sure to replace 'your_dataset_name.csv' with the actual file name created inside your data folder)
df = pd.read_csv("data/your_dataset_name.csv")

# Print the first 5 rows to make sure it loaded correctly
print("Data loaded successfully!")
print(df.head())