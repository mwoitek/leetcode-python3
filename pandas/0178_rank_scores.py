import numpy as np
import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    uniq_scores = np.sort(pd.unique(scores["score"]))[::-1]
    ranks = 1 + np.arange(len(uniq_scores), dtype=np.int_)
    df_ranks = pd.DataFrame(data={"score": uniq_scores, "rank": ranks})
    return (
        scores.merge(df_ranks, on="score")
        .sort_values(by="score", ascending=False)
        .loc[:, ["score", "rank"]]
    )
