import pandas as pd

aggregation_funs = {
    "mood": "mean",
    "circumplex.arousal": "mean",
    "circumplex.valence": "mean",
    "activity": "mean",
    "screen": "sum",
    "call": "sum",
    "sms": "sum",
    "appCat.builtin": "sum",
    "appCat.communication": "sum",
    "appCat.entertainment": "sum",
    "appCat.finance": "sum",
    "appCat.game": "sum",
    "appCat.office": "sum",
    "appCat.other": "sum",
    "appCat.social": "sum",
    "appCat.travel": "sum",
    "appCat.unknown": "sum",
    "appCat.utilities": "sum",
    "appCat.weather": "sum",
}


def agg_dates(df: pd.DataFrame, freq: str = "D") -> pd.DataFrame:
    # time key to group data
    time_key = pd.Grouper(freq=freq)

    return (
        df.pivot(index=["id", "time"], columns="variable", values="value")
        .reset_index()
        .set_index("time")
        .groupby(["id", time_key])
        .agg(aggregation_funs)
        .sort_index()
        .reset_index()
    )
