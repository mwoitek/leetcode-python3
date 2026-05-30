import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame,
) -> pd.DataFrame:
    max_salary = (
        employee.groupby(by="departmentId")
        .agg({"salary": "max"})
        .rename(columns={"salary": "max_salary"})
        .reset_index()
    )

    ans = employee.merge(max_salary, on="departmentId")
    ans = ans.loc[
        ans["salary"] == ans["max_salary"], ["name", "salary", "departmentId"]
    ].rename(columns={"name": "Employee", "salary": "Salary"})
    ans = (
        ans.merge(department, left_on="departmentId", right_on="id")
        .rename(columns={"name": "Department"})
        .loc[:, ["Department", "Employee", "Salary"]]
    )

    return ans
