# Debugging Note

## The error
While working on the file handling exercise (07), my script crashed with:

```
Traceback (most recent call last):
  Traceback (most recent call last):
  File "C:\Users\neche\Downloads\python-foundations-practice\07_file_handling\file_handling.py", line 32, in <module>
    data = read_scores("scores.txt")
  File "C:\Users\neche\Downloads\python-foundations-practice\07_file_handling\file_handling.py", line 12, in read_scores
    with open(path, "r") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'scores.txt'
```

## What caused it
I ran the script from the project root, but scores.txt is inside the 07_file_handling folder, so the relative path pointed to the wrong place.

## How I fixed it
I fixed it by building the path from the script’s location with pathlib:

```python
from pathlib import Path
BASE_DIR = Path(__file__).parent
read_scores(BASE_DIR / "scores.txt")
```

Now the script works no matter which folder I run it from.

## What I learned
Relative paths depend on the current working directory. Building paths from
`__file__` makes a script reliable.
