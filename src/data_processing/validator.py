from typing import Any, Callable, List, Optional

import pandas as pd
import pandera as pa

from data_processing import parser


class DataFrameSchema(pa.DataFrameSchema):
    pass


class Column(pa.Column):
    def __init__(
        self,
        *args: Any,
        parsers: Optional[List[Callable[..., Any]]] = None,
        **kwargs: Any
    ) -> None:
        self.parsers = [parser.default_parser]
        if parsers:
            self.parsers = parsers
        if "coerce" not in kwargs:
            kwargs["coerce"] = True
        super().__init__(*args, **kwargs)

    def parse(self, series: Any) -> pd.Series:
        for column_parser in self.parsers:
            series = column_parser(series)
        return series
