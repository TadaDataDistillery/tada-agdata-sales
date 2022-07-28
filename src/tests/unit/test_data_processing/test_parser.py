import unittest

from data_processing import parser


class TestParserSnakeCase(unittest.TestCase):
    def test_snake_case_converter(self):
        input_value = "  Caps Case  "
        expected_output = "caps_case"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_mixed(self):
        input_value = "CapsCase WithSpace"
        expected_output = "caps_case_with_space"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_camel(self):
        input_value = "camelCase"
        expected_output = "camel_case"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_camel_short(self):
        input_value = "PayToName"
        expected_output = "pay_to_name"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_camel_all_caps(self):
        input_value = "ABC"
        expected_output = "abc"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_camel_special_chars(self):
        input_value = "[some]! Extra? -Chars$"
        expected_output = "some_extra_chars"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_camel_lower_case(self):
        input_value = "some lower?case-phrase"
        expected_output = "some_lower_case_phrase"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)

    def test_snake_case_converter_camel_lower_case(self):
        input_value = "ON Arysta's DNC List?"
        expected_output = "on_arystas_dnc_list"
        output = parser.snake_case_converter(input_value)
        self.assertEqual(output, expected_output)


class TestParserBoolean(unittest.TestCase):
    def test_boolean_y(self):
        input_value = "  Y  "
        expected_output = True
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_yes(self):
        input_value = "yes  "
        expected_output = True
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_n(self):
        input_value = "N  "
        expected_output = False
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_no(self):
        input_value = " No  "
        expected_output = False
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_true(self):
        input_value = " true  "
        expected_output = True
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_false(self):
        input_value = " false  "
        expected_output = False
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_digit_true(self):
        input_value = " 1  "
        expected_output = True
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)

    def test_boolean_digit_false(self):
        input_value = " 0  "
        expected_output = False
        output = parser.string_to_bool(input_value)
        self.assertEqual(output, expected_output)
