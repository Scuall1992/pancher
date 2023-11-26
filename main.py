import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'report.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path, header=5)

# Display the DataFrame
print(df.count())
