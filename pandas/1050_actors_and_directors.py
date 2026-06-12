import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cnt = (
        actor_director.groupby(by=["actor_id", "director_id"])
        .agg(cnt=("timestamp", "count"))
        .reset_index()
    )
    return cnt.loc[cnt["cnt"] >= 3, ["actor_id", "director_id"]]
