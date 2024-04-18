from typing import Callable

import numpy as np
import pandas as pd

from utils import Column

TRANSFORM = {
    "mood": lambda x: x,
    "circumplex.arousal": lambda x: x,
    "circumplex.valence": lambda x: x,
    "activity": lambda x: x,
    "screen": lambda x: np.log(x),
    "call": lambda x: x,
    "sms": lambda x: x,
    "appCat.builtin": lambda x: np.log(x),
    "appCat.communication": lambda x: np.log(x),
    "appCat.entertainment": lambda x: np.log(x),
    "appCat.finance": lambda x: np.log(x),
    "appCat.game": lambda x: np.log(x),
    "appCat.office": lambda x: np.log(x),
    "appCat.other": lambda x: np.log(x),
    "appCat.social": lambda x: np.log(x),
    "appCat.travel": lambda x: np.log(x),
    "appCat.unknown": lambda x: np.log(x),
    "appCat.utilities": lambda x: np.log(x),
    "appCat.weather": lambda x: np.log(x),
}


# def apply_fun(row):
#    return TRANSFORM[row.variable]


def return_transformed(df: pd.DataFrame) -> pd.DataFrame:
    res = df.copy()
    res["transformed"] = res.apply(
        lambda row: TRANSFORM[row.variable](row.value), axis=1
    )
    return res
