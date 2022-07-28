import os
from typing import List, Optional

import awswrangler as wr
import pandas as pd


class FileWriter:
    def write_dataframe_to_parquet(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        partition_cols: Optional[List[str]] = None,
    ) -> None:
        raise NotImplementedError


class FileWriterLocal(FileWriter):
    def write_dataframe_to_parquet(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        partition_cols: Optional[List[str]] = None,
    ) -> None:
        del partition_cols
        dataframe.to_parquet(filename)


class FileWriterS3(FileWriter):
    def write_dataframe_to_parquet(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        partition_cols: Optional[List[str]] = None,
    ) -> None:
        prefix = "s3://"
        prefixed_filename = os.path.join(prefix, filename)
        wr.s3.to_parquet(
            dataframe,
            prefixed_filename,
            dataset=True,
            mode="overwrite_partitions",
            partition_cols=partition_cols,
        )
