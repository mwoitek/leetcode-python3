import numpy as np
import pandas as pd


def num_unique(col):
    return len(np.unique(col))


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return (
        teacher.groupby(by="teacher_id")
        .agg({"subject_id": num_unique})
        .reset_index()
        .rename(columns={"subject_id": "cnt"})
    )
