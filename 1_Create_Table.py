import os
import pandas as pd

# Path to the current directory (the directory where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# List of all files in the current directory
files_in_directory = os.listdir(current_directory)

# Filter only JPG files
jpg_files = [file for file in files_in_directory if file.lower().endswith(".jpg")]

# Create a Pandas DataFrame with file names
data = {"Filename": jpg_files}
df = pd.DataFrame(data)

# Path to the Excel file
excel_file = "All_Media.xlsx"

# Create an Excel table from the DataFrame
df.to_excel(excel_file, index=False)

print(f"All JPG files have been saved to {excel_file}.")
