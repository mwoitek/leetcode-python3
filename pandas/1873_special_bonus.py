import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    ans = employees[["employee_id"]]
    ans["bonus"] = 0
    mask = (employees["employee_id"] % 2 == 1) & (
        employees["name"].str.contains(r"^[^M]")
    )
    ans.loc[mask, "bonus"] = employees.loc[mask, "salary"]
    return ans.sort_values(by="employee_id")
