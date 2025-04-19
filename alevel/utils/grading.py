# O'Level Grading System
def grade_olevel(score):
    if score >= 85:
        return "D1"
    elif score >= 70:
        return "D2"
    elif score >= 65:
        return "C3"
    elif score >= 60:
        return "C4"
    elif score >= 55:
        return "C5"
    elif score >= 50:
        return "C6"
    elif score >= 45:
        return "P7"
    elif score >= 40:
        return "P8"
    else:
        return "F9"


# A'Level Grading System
def grade_alevel(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 45:
        return "E"
    else:
        return "F"


# A'Level Points Conversion Logic
def alevel_points(grade):
    grade_to_points = {
        "A": 6,
        "B": 5,
        "C": 4,
        "D": 3,
        "E": 2,
        "F": 0
    }
    return grade_to_points.get(grade, 0)

# Subsidiary Subject Point Logic
def subsidiary_points(score):
    """
    Returns 1 point for a subsidiary subject if passed (typically ≥ 50),
    otherwise returns 0.
    """
    return 1 if score >= 50 else 0

