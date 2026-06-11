import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    customer = (
        orders.groupby(by="customer_number").agg({"order_number": "count"}).idxmax()
    )
    return pd.DataFrame(data={"customer_number": customer})
