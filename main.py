import json

import pandas as pd
from pathlib import Path
from src.model import ISCWSACode

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

    parsed_df = [
        ISCWSACode.parse_data(code)
        for code in df.iterrows()
    ]
    # make a dictionary of the parsed data
    parsed_df = [code.model_dump() for code in parsed_df]
    # save the parsed data in a json file
    with open(resources_path / "parsed_data.json", "w") as f:
        json.dump(parsed_df, f, indent=2)

