import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    # Path to the data
    resources_path = Path(__file__).parent / "resources"
    file_name = "error-model-example-mwdrev5-1-iscwsa-1.xlsx"
    file_path = resources_path / file_name

    # Read the data
    df = pd.read_excel(
        file_path,
        sheet_name="Model",
        usecols="E:W",
        skiprows=2,
        nrows=41
    )
    print(df.columns)

