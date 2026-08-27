from pathlib import Path

import pandas as pd


# Read the workbook from the repository root into a new DataFrame.
excel_file = Path(__file__).resolve().parent / "Data" / "Soil_Autolabel_Data.xlsx"
soil_autolabel_df = pd.read_excel(excel_file)

print(f"Loaded {soil_autolabel_df.shape[0]} rows and {soil_autolabel_df.shape[1]} columns")
print(soil_autolabel_df.head())
