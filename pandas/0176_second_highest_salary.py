import numpy as np
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    uniq_salary = pd.unique(employee["salary"])
    s2 = None
    if len(uniq_salary) > 1:
        uniq_salary = np.sort(uniq_salary)
        s2 = uniq_salary[-2]
    return pd.DataFrame(data={"SecondHighestSalary": [s2]})
