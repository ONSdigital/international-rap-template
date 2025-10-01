---
applyTo: '**/*.py, **/*.r, **/*.R, **/*.rmd'
---

When generating code or documentation, follow these gold standard Reproducible Analytical Pipelines (RAP) principles:

### 📦 Modular Code
- Break code into small, reusable functions with clear, single responsibilities.
- Avoid side effects: functions should be referentially transparent—same inputs yield same outputs.
- Group related functions/classes into modules for clarity and reuse.
- Use scripts to orchestrate pipelines, keeping logic readable and reproducible.
- Prefer encapsulation over inheritance to reduce coupling and improve maintainability.

### ✍️ Readable Code
- Use informative, concise names for variables, functions, and classes.
  - Functions: start with verbs (e.g. `load_data`, `generate_report`).
  - Boolean-returning functions: use question-style names (e.g. `is_valid`, `has_errors`).
- Follow consistent style guides (e.g. PEP8 for Python, tidyverse for R).
- Write idiomatic code: use language-native patterns (e.g. list comprehensions in Python).
- Avoid repetition: refactor repeated logic into functions or classes.
- Be explicit: avoid relying on implicit truthiness or side effects.

### 🗒️ Code Documentation
- Use comments frequently, but only to explain *why* something is done, not *what* the code does.
- Avoid redundant or outdated comments; they mislead and reduce clarity.
- Use docstrings for functions, classes, and modules:
  - Describe purpose, parameters, return values, exceptions, usage examples.
  - Keep them up to date with code changes.
  - Follow consistent formatting (e.g. numpydoc, Google style, roxygen2).
- Avoid commented-out code; use configuration or control flow instead.
