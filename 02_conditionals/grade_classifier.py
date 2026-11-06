"""Exercise 2: conditionals. Turn a score into a grade and a remark."""


def classify(score):
    """Return (grade, remark) for a score from 0 to 100."""
    if score < 0 or score > 100:
        return None, "Invalid score: must be between 0 and 100"
    if score >= 70:
        return "A", "Excellent"
    elif score >= 60:
        return "B", "Very good"
    elif score >= 50:
        return "C", "Good"
    elif score >= 40:
        return "D", "Pass"
    else:
        return "F", "Fail"


if __name__ == "__main__":
    for s in [85, 65, 52, 41, 20, 120, -5]:
        grade, remark = classify(s)
        print(f"Score {s}: grade={grade}, remark={remark}")
