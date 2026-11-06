"""Exercise 7: file handling. Read scores, write a summary report."""

from pathlib import Path

# Build paths relative to THIS file, so the script works from any folder.
BASE_DIR = Path(__file__).parent


def read_scores(path):
    """Read 'name,score' lines and return a dictionary {name: score}."""
    scores = {}
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, score = line.split(",")
                scores[name] = int(score)
    return scores


def write_report(scores, path):
    """Write a summary of the scores to a new text file."""
    average = sum(scores.values()) / len(scores)
    best = max(scores, key=scores.get)
    with open(path, "w") as file:
        file.write(f"Students: {len(scores)}\n")
        file.write(f"Average score: {average:.1f}\n")
        file.write(f"Top student: {best} ({scores[best]})\n")


if __name__ == "__main__":
    data = read_scores(BASE_DIR / "scores.txt")
    write_report(data, BASE_DIR / "report.txt")
    print("Report written to report.txt")
