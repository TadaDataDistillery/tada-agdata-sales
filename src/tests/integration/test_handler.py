import unittest
from unittest import mock

from lambdas import handler, settings


class TestLambdaHandler(unittest.TestCase):
    def setUp(self):
        self.custom_settings = settings.SettingsFactory.local()

    @mock.patch("lambdas.settings.get_settings")
    def test_sales_report_handler(self, mocked_settings):
        mocked_settings.return_value = self.custom_settings
        handler.SALES_REPORT_FILENAME = "sales-report-small.xlsx"
        handler.sales_report_handler(None, None)

    @mock.patch("lambdas.settings.get_settings")
    def test_grower_extract_handler(self, mocked_settings):
        mocked_settings.return_value = self.custom_settings
        handler.GROWER_EXTRACT_FILENAME = "grower-extract-small.xlsx"
        handler.grower_extract_handler(None, None)
