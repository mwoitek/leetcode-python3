import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = pd.unique(views.loc[views["author_id"] == views["viewer_id"], "author_id"])
    return pd.DataFrame(data={"id": ids}).sort_values(by="id")
