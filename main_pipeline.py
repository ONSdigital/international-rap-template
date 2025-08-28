import pandas as pd
from scripts.validation_modules import validate_no_missing_values_excel
from scripts.processing_modules import calculate_column_mean

# Input Data

data_path = 'data/input_data.xlsx'  # Update with your actual file name
validate_no_missing_values_excel(data_path)
input_df = pd.read_excel(data_path)

# Run Processing Functions
# Example: Calculate the mean of a column (update 'Value1' as needed)
mean_value = calculate_column_mean(input_df, 'Value1')
print(f'Mean value: {mean_value}')

# Output Results
output_path = 'data/output_results.xlsx'
input_df['mean_value'] = mean_value
input_df.to_excel(output_path, index=False)
print(f'Results saved to {output_path}')
