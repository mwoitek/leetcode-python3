import numpy as np
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    s = None
    if N > 0 and len((uniq := pd.unique(employee["salary"]))) >= N:
        uniq = np.sort(uniq)
        s = uniq[-N]
    return pd.DataFrame(data={f"getNthHighestSalary({N})": [s]})
