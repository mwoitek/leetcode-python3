import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[
        (world["area"] >= int(3e6)) | (world["population"] >= int(2.5e7)),
        ["name", "population", "area"],
    ]
