import pandas as pd
import warnings
from scripts.validation_modules import validate_and_warn_missing

data_path = "data/input_data.xlsx"  # Update with your actual file name

# Find rows with missing values and print them so they can be checked manually
def main():
    validate_and_warn_missing(data_path)

if __name__ == "__main__":
    main()
