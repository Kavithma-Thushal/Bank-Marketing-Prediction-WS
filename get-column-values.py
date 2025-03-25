import pandas as pd

df = pd.read_csv("dataset/bank-marketing.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Ask for the column name
column_name = input("Enter the column name: ").strip()

# Check if the column exists in the dataset
if column_name in df.columns:
    # Handle the case for numeric columns
    if pd.api.types.is_numeric_dtype(df[column_name]):
        data = ",".join(map(str, df[column_name].dropna().astype(int)))
    else:
        # Handle non-numeric columns
        data = ",".join(df[column_name].dropna().astype(str))

    if not data:
        print(f"No data found for the column '{column_name}'.")
    else:
        print(data)

else:
    print(f"Column '{column_name}' not found in dataset.")
