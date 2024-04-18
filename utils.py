import os

import pandas as pd


class Column:
    ID = "id"
    TIME = "time"
    VARIABLE = "variable"
    VALUE = "value"


class Variable:
    MOOD = "mood"
    AROUSAL = "circumplex.arousal"
    VALENCE = "circumplex.valence"
    ACTIVITY = "activity"
    SCREEN = "screen"
    CALL = "call"
    SMS = "sms"
    BUILTIN = "appCat.builtin"
    COMMUNICATION = "appCat.communication"
    ENTERTAINMENT = "appCat.entertainment"
    FINANCE = "appCat.finance"
    GAME = "appCat.game"
    OFFICE = "appCat.office"
    OTHER = "appCat.other"
    SOCIAL = "appCat.social"
    TRAVEL = "appCat.travel"
    UNKNOWN = "appCat.unknown"
    UTILITIES = "appCat.utilities"
    WEATHER = "appCat.weather"

    @classmethod
    def variables(cls):
        is_valid = lambda x, y: isinstance(y, str) and "_" not in x
        return [value for key, value in vars(cls).items() if is_valid(key, value)]


def load(filename: str) -> pd.DataFrame:
    return pd.read_csv(
        os.path.join("data", os.path.basename(filename)),
        usecols=[Column.ID, Column.TIME, Column.VARIABLE, Column.VALUE],
        parse_dates=[Column.TIME],
    )


def check_variable(v: str) -> str:
    assert v in Variable.variables(), f"Variable {v} doesn't exist in data"
    return v
