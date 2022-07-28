import os
from typing import Any, Dict

import pandas as pd

from data_processing import processor, schema, validator
from lambdas import settings as lambda_settings

SALES_REPORT_FILENAME: str = "sales-report.xlsx"
GROWER_EXTRACT_FILENAME: str = "grower-extract.xlsx"


def sales_report_handler(event: Dict[str, Any], context: Any) -> None:
    del event, context
    settings = lambda_settings.get_settings()
    settings.logger.debug("Running sales report handler...")
    filename = os.path.join(
        settings.raw_bucket, settings.raw_prefix, SALES_REPORT_FILENAME
    )
    settings.logger.debug("Reading file...")
    raw_dataframes: Dict[str, pd.DataFrame] = settings.file_reader.read_dataframe(
        filename, sheet_name=None
    )
    target_schema = schema.sales_report_schema
    output_prefix: str = "sales_report"
    process_sheets(raw_dataframes, target_schema, output_prefix, settings)
    settings.logger.debug("Done")


def grower_extract_handler(event: Dict[str, Any], context: Any) -> None:
    del event, context
    settings = lambda_settings.get_settings()
    settings.logger.debug("Running growers extract handler...")
    filename = os.path.join(
        settings.raw_bucket, settings.raw_prefix, GROWER_EXTRACT_FILENAME
    )
    settings.logger.debug("Reading file...")
    raw_dataframes: Dict[str, pd.DataFrame] = settings.file_reader.read_dataframe(
        filename, sheet_name=None
    )
    target_schema = schema.growers_extract_schema
    output_prefix: str = "growers_extract"
    process_sheets(raw_dataframes, target_schema, output_prefix, settings)
    settings.logger.debug("Done")


def process_sheets(
    raw_dataframes: Dict[str, pd.DataFrame],
    target_schema: Dict[str, validator.DataFrameSchema],
    output_prefix: str,
    settings: lambda_settings.Settings,
) -> None:
    raw_dataframes = processor.process_sheet_names(raw_dataframes)
    for sheet_name in target_schema:
        settings.logger.debug(f"Processing sheet {sheet_name} for {output_prefix}...")
        processed_dataframe = processor.process_dataframe_sheet(
            raw_dataframes[sheet_name], target_schema[sheet_name]
        )
        settings.logger.debug("Validating...")
        target_schema[sheet_name].validate(processed_dataframe)
        settings.logger.debug("Writing...")
        output_filename = os.path.join(
            settings.output_bucket,
            settings.output_prefix,
            output_prefix,
            sheet_name,
        )
        settings.file_writer.write_dataframe_to_parquet(
            processed_dataframe, output_filename, partition_cols=None
        )
