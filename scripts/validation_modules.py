

"""
Data Validation Module
----------------------
Why perform data validation before starting a pipeline?

Data validation ensures that input data meets the required quality, format, and
integrity standards before processing. This helps to:
- Prevent errors and crashes during pipeline execution
- Ensure reliable and accurate results
- Save time by catching issues early
- Improve reproducibility and maintainability
"""

import pandas as pd
import warnings
import os
from datetime import datetime
def validate_and_warn_missing(excel_path, sheet_name=0, columns=None):
    """
    Validates an Excel sheet for missing values in specified columns and issues warnings if any are found.
    Additionally, if missing values are found, saves a copy of the sheet with a '_revisedYYYYMMDD' suffix
    and prints a clickable link to the new file.

    Parameters:
        excel_path (str): Path to the Excel file to be validated.
        sheet_name (int or str, optional): Name or index of the sheet to read. Defaults to the first sheet (0).
        columns (list or None, optional): List of column names to check for missing values. If None, all columns are checked.

    Behavior:
        - Reads the specified Excel sheet into a DataFrame.
        - Checks for missing (NaN) values in the specified columns.
        - If missing values are found:
            - Prints a warning with the names of columns containing missing values.
            - Prints the rows that contain missing values in those columns.
            - Issues a warning using the warnings module.
            - Saves a copy of the Excel sheet with '_revisedYYYYMMDD' appended to the filename.
            - Prints a clickable link to the revised file.
        - If no missing values are found, prints a confirmation message.

    Raises:
        FileNotFoundError: If the specified Excel file does not exist.
        ValueError: If specified columns are not found in the DataFrame.
    """
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    if columns is None:
        columns = df.columns
    missing = df[columns].isnull().sum()
    missing_cols = missing[missing > 0]
    if not missing_cols.empty:
        print("Warning: Missing values found in columns:", list(missing_cols.index))
        print("Rows with missing values:")
        rows_with_missing = df[df[missing_cols.index].isnull().any(axis=1)]
        print(rows_with_missing)
        warnings.warn("Data contains missing values. Please review the output above.")

        # Save revised file
        base, ext = os.path.splitext(excel_path)
        datestamp = datetime.now().strftime("%Y%m%d")
        revised_path = f"{base}_revised{datestamp}{ext}"
        df.to_excel(revised_path, index=False)
        # Print clickable link (works in Jupyter and some terminals)
        print(f"Revised file saved: {revised_path}")
        print(f"Click here to open: file://{os.path.abspath(revised_path)}")
    else:
        print("No missing values found. Data is valid.")



def compare_columns(df: pd.DataFrame, col1: str, col2: str) -> pd.Series:
    """
    Compares two columns in the DataFrame and returns a boolean Series indicating
    whether the values in each row are equal.

    Args:
        df (pd.DataFrame): The validated input DataFrame.
        col1 (str): The name of the first column to compare.
        col2 (str): The name of the second column to compare.

    Returns:
        pd.Series: Boolean Series where True indicates the values are equal.

    Raises:
        KeyError: If either column does not exist in the DataFrame.
    """
    if col1 not in df.columns or col2 not in df.columns:
        raise KeyError(f"Both '{col1}' and '{col2}' must exist in the DataFrame.")
    return df[col1] == df[col2]
