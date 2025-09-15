import pandas as pd
from scripts.utility_modules import ensure_parent_folder_exists 
from scripts.validation_modules import validate_and_warn_missing
from scripts.processing_modules import calculate_row_means
from config import revised_data_path, output_path

def main():
    """
    Entry point for the pipeline.

    This function performs the following steps:
    1. Validates the input Excel file for missing values and warns if any are found.
    2. Loads the validated data into a pandas DataFrame.
    3. Processes the data by calculating the mean across specified columns for each row.
    4. Ensures the parent directory for the output file exists.
    5. Writes the processed results to an Excel file.
    
    """
    # check there are no missing values
    validate_and_warn_missing(revised_data_path)
    input_df = pd.read_excel(revised_data_path)

    # Run Processing Functions
    # Example: Calculate the mean of a row across specified columns
    output_df = calculate_row_means(input_df, ['Value1', 'Value2'])

    # Ensure output folder exists before saving
    ensure_parent_folder_exists(output_path)

    # Output Results
    output_df.to_excel(output_path, index=False)
    print(f'Results saved to {output_path}')

if __name__ == "__main__":
    main()
