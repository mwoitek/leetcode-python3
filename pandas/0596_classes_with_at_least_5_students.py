import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by="class").agg(cnt=("student", "count")).reset_index()
    return df.loc[df["cnt"] >= 5, ["class"]]
