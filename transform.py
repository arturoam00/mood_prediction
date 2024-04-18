import numpy as np
import pandas as pd

transformation_funs = {
    "screen": np.log,
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
    res["transformed"] = res.apply(
        lambda row: transformation_funs.get(row.variable, lambda x: x)(row.value),
        axis=1,
    )
    return res
