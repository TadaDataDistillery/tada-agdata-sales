import logging
import os
from dataclasses import dataclass

from data_processing.file import reader, writer

LOGGING_LEVEL: str = os.environ.get("LOGGING_LEVEL", "DEBUG")


def get_logger(name: str, level: str) -> logging.Logger:
    logging_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logger: logging.Logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        logger.propagate = False
        formatter = logging.Formatter(logging_format)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger


@dataclass
class Settings:
    raw_prefix: str
    output_prefix: str
    raw_bucket: str
    output_bucket: str
    file_reader: reader.FileReader
    file_writer: writer.FileWriter
    logger: logging.Logger


class SettingsFactory:
    @staticmethod
    def aws() -> Settings:
        raw_prefix: str = os.environ["RAW_PREFIX"]
        output_prefix: str = os.environ["OUTPUT_PREFIX"]
        raw_bucket: str = os.environ["RAW_BUCKET"]
        output_bucket: str = os.environ["OUTPUT_BUCKET"]
        logger = get_logger("handler", LOGGING_LEVEL)

        return Settings(
            raw_prefix,
            output_prefix,
            raw_bucket,
            output_bucket,
            reader.FileReaderS3(),
            writer.FileWriterS3(),
            logger,
        )

    @staticmethod
    def local() -> Settings:
        raw_prefix: str = os.path.join("data", "raw")
        output_prefix: str = os.path.join("data", "output")
        logger = get_logger("handler", LOGGING_LEVEL)

        return Settings(
            raw_prefix,
            output_prefix,
            "",
            "",
            reader.FileReaderLocal(),
            writer.FileWriterLocal(),
            logger,
        )


def get_settings() -> Settings:
    if "STAGE" not in os.environ:
        return SettingsFactory.local()
    return SettingsFactory.aws()
