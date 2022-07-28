import re
from typing import Optional

import pandas as pd


def default_parser(series: pd.Series) -> pd.Series:
    return series


def snake_case_converter(value: str) -> str:
    # fix apostrophes
    value = re.sub(r"([a-zA-Z])['\"]s", r"\1s", value)
    # replace special chars and whitespace with caps case
    # i.e. " some-valueHere" -> "SomeValueHere"
    split_token = "*"
    value = re.sub(r"[^\da-zA-Z]", split_token, value)
    raw_tokens = value.split(split_token)
    parsed_tokens = []
    for item in raw_tokens:
        if item.upper() == item or len(item) == 1:
            parsed_tokens.append(item.capitalize())
        else:
            parsed_tokens.append(item[0].upper() + item[1:])
    value = "".join(parsed_tokens)
    value = value.replace(" ", "")
    # special case for all caps values
    # i.e. "ABC" -> "abc"
    if re.match(r"^[A-Z]+$", value):
        return value.lower()
    # convert caps/camel case to camel case
    return re.sub(r"(.{1})([A-Z])", r"\1_\2", value).lower()


def parse_phone_number(number: Optional[str]) -> Optional[str]:
    if number is not None:
        return re.sub(r"[+()\- ]", "", number)
    return None


def parse_phone_numbers(series: pd.Series) -> pd.Series:
    series = series.astype(str)
    series = series.apply(parse_phone_number)
    return series


def string_to_bool(value: Optional[str]) -> Optional[bool]:
    if not value:
        return None
    value = value.lower().replace(" ", "")
    if "t" in value:
        return True
    if "y" in value:
        return True
    if value == "1":
        return True
    return False


def parse_boolean(series: pd.Series) -> pd.Series:
    series = series.astype(str)
    series = series.apply(string_to_bool)
    return series
