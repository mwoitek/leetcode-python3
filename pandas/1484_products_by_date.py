import numpy as np
import pandas as pd


def get_product_list(products):
    uniq = np.unique(products)
    return ",".join(uniq)


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return (
        activities.groupby(by="sell_date")
        .agg(num_sold=("product", "nunique"), products=("product", get_product_list))
        .reset_index()
        .sort_values(by="sell_date")
    )
