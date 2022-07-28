import io
import os
from typing import Any

import boto3
import pandas as pd


class FileReader:
    def get_filename_prefix(self) -> str:
        raise NotImplementedError

    def read_bytes(self, filename: str) -> bytes:
        raise NotImplementedError

    def read_dataframe(self, filename: str, **kwargs: Any) -> pd.DataFrame:
        prefixed_filename: str = os.path.join(self.get_filename_prefix(), filename)
        raw_data: bytes = self.read_bytes(prefixed_filename)
        file_data: io.BytesIO = io.BytesIO(raw_data)
        if filename.endswith(".csv"):
            return pd.read_csv(file_data, **kwargs)
        if filename.endswith(".xlsx"):
            return pd.read_excel(file_data, **kwargs)
        raise ValueError("Filename extension not supported")


class FileReaderLocal(FileReader):
    def get_filename_prefix(self) -> str:
        return ""

    def read_bytes(self, filename: str) -> bytes:
        with open(filename, "rb") as file_object:
            return file_object.read()


class FileReaderS3(FileReader):
    def __init__(self) -> None:
        self.s3_resource = boto3.resource("s3")

    def get_filename_prefix(self) -> str:
        return "s3://"

    def read_bytes(self, filename: str) -> bytes:
        bucket = filename.split("/")[2]
        key = filename.split(bucket)[-1].lstrip("/")
        try:
            response = self.s3_resource.Object(bucket, key).get()
        except Exception as exception:
            raise Exception(
                f"Could not open key {key} in bucket {bucket}: {exception}"
            ) from exception
        file_bytes: bytes = response["Body"].read()
        return file_bytes
