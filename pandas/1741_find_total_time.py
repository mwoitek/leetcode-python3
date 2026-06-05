import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees.assign(delta_time=lambda x: x["out_time"] - x["in_time"])
        .groupby(by=["event_day", "emp_id"])
        .agg({"delta_time": "sum"})
        .reset_index()
        .rename(columns={"event_day": "day", "delta_time": "total_time"})
    )
