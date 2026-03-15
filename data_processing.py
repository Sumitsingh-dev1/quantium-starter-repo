import pandas as pd
import glob
import os

files = glob.glob(os.path.join("data", "*.csv"))
print("Files found:", files)

dfs = []

for file in files:
    df = pd.read_csv(file)

    df["product"] = df["product"].astype(str).str.lower().str.strip()
    df = df[df["product"] == "pink morsel"]

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = df["price"].replace("[$,]", "", regex=True)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df["Sales"] = df["quantity"] * df["price"]

    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]

    dfs.append(df)

if dfs:
    final_df = pd.concat(dfs, ignore_index=True)
    final_df.to_csv("formatted_output.csv", index=False)
    print("formatted_output.csv created successfully")
else:
    print("No CSV files found in the data folder.")