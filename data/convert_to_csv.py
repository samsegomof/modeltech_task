import pandas as pd

read_sheet_rates = pd.read_excel('well_data.xlsx', sheet_name='rates')
read_sheet_rates.to_csv('rates.csv', index=False)

read_sheet_splits = pd.read_excel('well_data.xlsx', sheet_name='splits')
read_sheet_splits.to_csv('splits.csv', index=False)

read_sheet_invalid_splits = pd.read_excel('well_data.xlsx', sheet_name='invalid_splits')
read_sheet_invalid_splits.to_csv('invalid_splits.csv', index=False)
