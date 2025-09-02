import pandas as pd
import warnings
from scripts.validation_modules import validate_and_warn_missing
from config import data_path

# Find rows with missing values and print them so they can be checked manually
def main():
    validate_and_warn_missing(data_path)

if __name__ == "__main__":
    main()
