from typing import Literal

import pandas as pd

from utils import Column

hours_cond = lambda s: (0 <= s) & (s <= 7200)

outliers_conds = {
    "mood": lambda x: (0 <= x) & (x <= 10),
    "circumplex.arousal": lambda x: (-2 <= x) & (x <= 2),
    "circumplex.valence": lambda x: (-2 <= x) & (x <= 2),
    "activity": lambda x: (0 <= x) & (x <= 1),
    "screen": lambda x: x >= 0,
    "call": lambda x: x == 1,
    "sms": lambda x: x == 1,
    "appCat.builtin": lambda x: x >= 0,
    "appCat.communication": hours_cond,
    "appCat.entertainment": hours_cond,
    "appCat.finance": hours_cond,
    "appCat.game": hours_cond,
    "appCat.office": hours_cond,
    "appCat.other": hours_cond,
    "appCat.social": hours_cond,
    "appCat.travel": hours_cond,
    "appCat.unknown": hours_cond,
    "appCat.utilities": hours_cond,
    "appCat.weather": hours_cond,
}


def remove_duplicates(
    df: pd.DataFrame, keep: Literal["first", "last", False] = False
) -> pd.DataFrame:
    """
    For rows like:

    135,2014-04-17 11:00:00,AS14.01,mood,7.0
    136,2014-04-17 11:00:00,AS14.01,mood,6.0

    we keep the last value (would be 6.0 here)

    Using pd.DataFrame.drop_duplicates() is *not* sufficient for this
    """
    return df.drop(
        df[df[[Column.ID, Column.TIME, Column.VARIABLE]].duplicated(keep=keep)].index
    )


def fill_missing(df: pd.DataFrame, limit: int = 5) -> pd.DataFrame:
    """
    First group by `id` and `variable`, see if there are NA values
    and fill forward up to `limit`. Remove remaining rows with NA
    values
    Both `bfill` and `ffill` work, the first achives to fill one
    more row than the second (row: 14213 in original)
    """
    return (
        df.groupby([Column.ID, Column.VARIABLE])
        .apply(func=lambda g: g.bfill(limit=limit), include_groups=False)
        .reset_index()
        .sort_values(by="level_2")
        .reset_index(drop=True)
        .drop(columns="level_2")
        .dropna()
    )


def filter_outliers(df: pd.DataFrame) -> pd.DataFrame:
    drop = []
    for v in outliers_conds:
        mask = df[df[Column.VARIABLE] == v][Column.VALUE].apply(outliers_conds[v])
        drop.extend(list(mask[mask == False].index))
    return df.drop(index=drop)
