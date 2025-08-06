"""
Processing Modules
------------------
This module contains functions that perform the main processing steps of the pipeline.
These functions should intake validated data, perform calculations or transformations,
and output the results. Data passed to these functions should already be validated.

Example: A function that calculates the mean of a numeric column in a DataFrame.
"""

import pandas as pd

def calculate_column_mean(df: pd.DataFrame, column: str) -> float:
    """
    Calculates the mean of a specified numeric column in the DataFrame.

    Args:
        df (pd.DataFrame): The validated input DataFrame.
        column (str): The name of the column to calculate the mean for.

    Returns:
        float: The mean value of the column.

    Raises:
        KeyError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"Column '{column}' must be numeric.")
    return df[column].mean()
