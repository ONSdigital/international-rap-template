# Copilot Instructions for AI Coding Agents

This repository is a template for reproducible analytical pipelines (RAP) aimed at international projects and external stakeholders. It is intentionally minimal, focusing on clarity and ease of use for those new to RAP and version control.

## Architecture Overview
- **Main workflow:**
  - `data_input_validation.py`: Validates input data before processing.
  - `main_pipeline.py`: Runs the main data processing pipeline after validation.
- **Modules:**
  - `scripts/validation_modules.py`: Data validation functions.
  - `scripts/processing_modules.py`: Data processing functions.
- **Configuration:**
  - `config.py`: Central location for paths and parameters. Update `revised_data_path` after data correction.
- **Data:**
  - `demonstration_data/input_data.xlsx`: Example input for demonstration.
  - `data/`: User-provided input and output files (not versioned).
  - `outputs/`: Generated output files (not versioned).

## Developer Workflows
- **Environment setup:**
  - Use Python 3.12 and create a virtual environment (`python -m venv venv`).
  - Activate with `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux).
  - Install dependencies: `pip install -r demonstration_requirements.txt`.
- **Running the pipeline:**
  1. Run validation: `python data_input_validation.py`.
  2. Manually correct missing values in the revised file.
  3. Update `config.py` with the new file path.
  4. Run main pipeline: `python main_pipeline.py`.
- **No automated tests or CI/CD** are present; manual validation and stepwise execution are required.

## Project-Specific Patterns
- **Explicit stepwise workflow:** Validation and processing are separate; manual intervention is expected between steps.
- **Minimal dependencies:** Only those listed in `demonstration_requirements.txt` are required for the example.
- **No outputs or data files are versioned.**
- **Documentation-first:** Users are encouraged to update `readme_template.md` for their own projects.

## Integration Points
- No external APIs or services are integrated; all processing is local and file-based.
- Extend the template for advanced features (testing, CI, containerization) as needed.

## Key Files & Directories
- `main_pipeline.py`, `data_input_validation.py`, `config.py`
- `scripts/validation_modules.py`, `scripts/processing_modules.py`
- `demonstration_data/`, `data/`, `outputs/`

## Example: Data Validation and Processing
```bash
python data_input_validation.py
# Manually correct missing values in the revised file
# Update config.py with new path
python main_pipeline.py
```

---
For questions about unclear workflows or conventions, consult `README.md` or ask for clarification.
