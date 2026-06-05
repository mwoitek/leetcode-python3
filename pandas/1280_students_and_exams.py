import pandas as pd


def students_and_examinations(
    students: pd.DataFrame,
    subjects: pd.DataFrame,
    examinations: pd.DataFrame,
) -> pd.DataFrame:
    df1 = students.merge(subjects, how="cross")
    df2 = (
        students.merge(examinations, on="student_id")
        .groupby(by=["student_id", "subject_name"])
        .agg(attended_exams=("student_id", "count"))
        .reset_index()
    )
    ans = df1.merge(df2, how="left", on=("student_id", "subject_name")).sort_values(
        by=["student_id", "subject_name"]
    )
    ans["attended_exams"].fillna(0, inplace=True)
    return ans
