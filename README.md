# Python Foundations Practice (B1)

Eight small Python exercises built for the FlexiSAF Internship Program,
AI Engineering pathway, Module B1.

Author: Chinecherem Ude

## Requirements
- Python 3.11 or newer
- Git

## Setup
```bash
git clone <your-repo-url>
cd python-foundations-practice
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Exercises and how to run them
| # | Folder | Concept | Run |
|---|--------|---------|-----|
| 1 | `01_variables_data_types` | Variables and data types | `python 01_variables_data_types/student_profile.py` |
| 2 | `02_conditionals` | Conditionals | `python 02_conditionals/grade_classifier.py` |
| 3 | `03_loops` | Loops | `python 03_loops/loops_demo.py` |
| 4 | `04_functions` | Functions (tested) | `python 04_functions/functions.py` |
| 5 | `05_modules` | Modules | `cd 05_modules && python main.py` |
| 6 | `06_error_handling` | Error handling | `python 06_error_handling/safe_calculator.py` |
| 7 | `07_file_handling` | File handling (tested) | `python 07_file_handling/file_handling.py` |
| 8 | `08_script_organisation` | Script organisation | `python 08_script_organisation/expense_tracker.py` |

## Running the tests
From the repo root:
```bash
pytest
```
Tests exist for exercise 4 (functions) and exercise 7 (file handling).

## Formatting
```bash
black .
```

## Debugging note
See [DEBUGGING_NOTE.md](DEBUGGING_NOTE.md).
