import numpy as np
import pandas as pd

from utils import Column


def log(x: pd.Series) -> pd.Series:
    pass


transformation_funs = {
    "mood": lambda x: x,
    "circumplex.arousal": lambda x: x,
    "circumplex.valence": lambda x: x,
    "activity": lambda x: x,
    "screen": np.log,
    "call": lambda x: x,
    "sms": lambda x: x,
    "appCat.builtin": np.log,
    "appCat.communication": np.log,
    "appCat.entertainment": np.log,
    "appCat.finance": np.log,
    "appCat.game": np.log,
    "appCat.office": np.log,
    "appCat.other": np.log,
    "appCat.social": np.log,
    "appCat.travel": np.log,
    "appCat.unknown": np.log,
    "appCat.utilities": np.log,
    "appCat.weather": np.log,
}


def return_transformed(df: pd.DataFrame) -> pd.DataFrame:
    res = df.copy()
    res[Column.TRANSFORMED] = res.apply(
        lambda row: transformation_funs.get(row.variable, lambda x: x)(row.value),
        axis=1,
    )
    return res.drop(columns=Column.VALUE).rename(
        columns={Column.TRANSFORMED: Column.VALUE}
    )

