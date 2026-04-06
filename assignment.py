import pandas as pd

# =========================
# TASK 1: Read CSV File
# =========================
def load_data():
    """
    Reads 'data.csv' and returns a Pandas DataFrame.

    Returns:
        pd.DataFrame
    """
    return pd.read_csv("data.csv")


# =========================
# TASK 2: Average Marks
# =========================
def average_marks(df):
    """
    Calculates the average marks.

    Args:
        df (pd.DataFrame): Input data

    Returns:
        float: Average marks
    """
    return df["marks"].mean()


# =========================
# TASK 3: Top Student
# =========================
def top_student(df):
    """
    Finds the student with highest marks.

    Args:
        df (pd.DataFrame): Input data

    Returns:
        str: Name of top student
    """
    top_row = df.loc[df["marks"].idxmax()]
    return top_row["name"]


# =========================
# TASK 4: Passed Students
# =========================
def passed_students(df):
    """
    Filters students who passed (marks >= 50).

    Args:
        df (pd.DataFrame): Input data

    Returns:
        pd.DataFrame
    """
    return df[df["marks"] >= 50]


# =========================
# TASK 5: Add Grade Column
# =========================
def add_grade(df):
    """
    Adds a new column 'grade' based on marks:
        A: >= 75
        B: >= 50
        C: < 50

    Args:
        df (pd.DataFrame): Input data

    Returns:
        pd.DataFrame
    """
    df = df.copy()
    df["grade"] = df["marks"].apply(
        lambda marks: "A" if marks >= 75 else ("B" if marks >= 50 else "C")
    )
    return df
