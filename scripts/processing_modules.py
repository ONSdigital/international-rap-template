"""
Processing Modules
------------------
This module contains functions that perform the main processing steps of the pipeline.
These functions should intake validated data, perform calculations or transformations,
and output the results. Data passed to these functions should already be validated.
"""

import pandas as pd

def calculate_row_means(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Calculates the mean across specified numeric columns for each row and adds the result to a new column 'mean'.

    Args:
        df (pd.DataFrame): The validated input DataFrame.
        columns (list[str]): The list of column names to calculate the mean across.

    Returns:
        pd.DataFrame: The DataFrame with a new column 'mean' containing the row-wise means.

    Raises:
        KeyError: If any column does not exist in the DataFrame.
        TypeError: If any column is not numeric.
    """
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Columns {missing_cols} not found in DataFrame.")
    non_numeric = [col for col in columns if not pd.api.types.is_numeric_dtype(df[col])]
    if non_numeric:
        raise TypeError(f"Columns {non_numeric} must be numeric.")
    df = df.copy()
    df["mean"] = df[columns].mean(axis=1)
    return df
