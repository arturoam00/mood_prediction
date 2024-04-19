from typing import Any, Callable

import matplotlib.pyplot as plt
import pandas as pd

from utils import Column, Variable, check_variable


def get_values(df: pd.DataFrame, variable: str) -> pd.Series:
    variable = check_variable(variable)
    return df[df[Column.VARIABLE] == variable][Column.VALUE]


"""

def plot_hist(
    df: pd.DataFrame,
    variable: str,
    t: Callable[..., pd.Series] = lambda x: x,
    t_params: dict[str, Any] = {},
    **kwargs,
) -> None:
    values = t(get_values(df, variable), **t_params)
    plt.hist(values, **kwargs)
    plt.show()


def plot_scatter_mood(
    df: pd.DataFrame,
    variable: str,
    t: Callable[..., pd.Series] = lambda x: x,
    t_params: dict[str, Any] = {},
    **kwargs,
):
    values = t(get_values(df, variable), **t_params)
    plt.scatter(x=values, y=get_values(df, Variable.MOOD), **kwargs)
    plt.show()


def plot_boxplot(df: pd.DataFrame, variable: str) -> None:
    values = get_values(df, variable)
    plt.boxplot(values)
    plt.show()

"""
