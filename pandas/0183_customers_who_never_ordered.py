import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    unique_ids = pd.unique(orders["customerId"])
    return customers.loc[~(customers["id"].isin(unique_ids)), ["name"]].rename(
        columns={"name": "Customers"}
    )
