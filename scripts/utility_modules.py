"""
Utility Modules
---------------
This module provides utility functions to support the pipeline, such as file and directory management.
These functions are designed to be reusable, modular, and to handle common tasks that are not specific
to data processing or analysis, but are essential for reproducible workflows.

Functions included:
- ensure_parent_folder_exists: Ensures the parent directory for a given file path exists, creating it if necessary.
"""

import os

def ensure_parent_folder_exists(file_path):
    """
    Ensure the parent folder of the given file path exists.

    Parameters
    ----------
    file_path : str
        The path to the file for which the parent directory should be checked/created.

    Returns
    -------
    None

    Raises
    ------
    OSError
        If the directory cannot be created due to a system error.

    Example
    -------
    >>> ensure_parent_folder_exists('data/results/output.xlsx')
    # Creates 'data/results' if it does not exist.
    """
    parent_folder = os.path.dirname(file_path)
    if parent_folder and not os.path.exists(parent_folder):
        os.makedirs(parent_folder)