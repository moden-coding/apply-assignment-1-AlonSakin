import pandas as pd
import numpy as np

def assign_letter_grades(df):
    df["Grade"] = df["Exam_Score"].apply(lambda g: 'A' if g >= 90 else ('B' if g >= 80 else ('C' if g >= 70 else 'D')))

    return df


def calculate_adjusted_score(df):
    df["Adjusted_Score"] = df.apply(lambda r: r['Exam_Score'] + r['Study_Hours'] * 1.5 + r['Attendance'] * 10, axis=1)

    return df


def categorize_performance(df):
    df["Performance"] = df.apply(lambda row: 'Outstanding' if row["Grade"] == 'A' else ("Strong" if row["Grade"] == 'B' else ("Needs Improvement" if row["Grade"] in ['C', 'D'] else "Average")), axis=1)
    
    return df



# Sample dataset
df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Ella", "Frank"],
    "Exam_Score": [85, 72, 90, 64, 78, 95],
    "Study_Hours": [6, 3, 8, 2, 4, 10],
    "Attendance": [0.95, 0.80, 0.90, 0.70, 0.75, 0.98]
})

print(assign_letter_grades(df))

