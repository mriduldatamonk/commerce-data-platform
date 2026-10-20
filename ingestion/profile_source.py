from pathlib import Path
import pandas as pd

RAW_DIR = Path("C:\\Users\\mridulsharma2\\Downloads\\Olist_Ecommerce_Phase1\\commerce-data-platform\\data\\raw")

def profile_file(file_path: Path):
    df = pd.read_csv(file_path)

    print(f"\n{'='* 80}")
    print(f"FILE: {file_path.name}")
    print(f"{'='* 80}")


    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumns:")
    for column in df.columns:
        print(f" - {column}")

    print("\nData Types:")
    print(df.dtypes)


    print("\nNull Counts:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


for file_path in RAW_DIR.glob("*.csv"):
    profile_file(file_path)