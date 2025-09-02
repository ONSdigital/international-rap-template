import pandas as pd
from scripts.validation_modules import validate_and_warn_missing
from scripts.processing_modules import calculate_row_means
from config import revised_data_path, output_path

def main():
    # check there are no missing values
    validate_and_warn_missing(revised_data_path)
    input_df = pd.read_excel(revised_data_path)

    # Run Processing Functions
    # Example: Calculate the mean of a row across specified columns
    output_df = calculate_row_means(input_df, ['Value1', 'Value2'])

    # Output Results
    output_df.to_excel(output_path, index=False)
    print(f'Results saved to {output_path}')

if __name__ == "__main__":
    main()
