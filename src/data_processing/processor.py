from typing import Dict

import pandas as pd

from data_processing import parser, validator


def process_dataframe_sheet(
    dataframe: pd.DataFrame, sheet_schema: validator.DataFrameSchema
) -> pd.DataFrame:
    dataframe = process_column_names(dataframe)
    schema_columns = sheet_schema.columns
    dataframe = dataframe[schema_columns.keys()]
    for column in schema_columns:
        series: pd.Series = dataframe[column]
        if schema_columns[column].coerce:
            dataframe[column] = schema_columns[column].dtype(dataframe[column])
        dataframe[column] = schema_columns[column].parse(series)  # type: ignore

    return dataframe


def process_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    column_mappings: Dict[str, str] = {}
    for column_name in dataframe.columns:
        column_mappings[column_name] = parser.snake_case_converter(column_name)
    dataframe = dataframe.rename(columns=column_mappings)
    return dataframe


def process_sheet_names(dataframes: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    original_sheet_names = list(dataframes.keys())
    for sheet_name in original_sheet_names:
        processed_sheet_name = parser.snake_case_converter(sheet_name)
        dataframes[processed_sheet_name] = dataframes[sheet_name]
        del dataframes[sheet_name]
    return dataframes
