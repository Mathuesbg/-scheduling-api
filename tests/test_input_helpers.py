from unittest import TestCase
from unittest.mock import patch
from utils.input_helpers import get_valid_index_input, get_valid_input

def validator_mock(value):
    return value == "ok"

def index_validator_mock(value, menu):

    return value == "2"

class TestInputHelpers(TestCase):

    @patch("builtins.input", side_effect=["wrong", "ok"])
    def test_get_valid_input_returns_a_valid_value(self, mock):

        value = get_valid_input("test :", validator_mock)
        self.assertEqual(value, "ok")

    @patch("builtins.input", side_effect=["a", "-1", "2", "3"])
    def test_get_valid_index_input_returns_a_valid_value(self, mock):
        
        menu = {
            0 : "2025-04-07T14:30:00.000Z",
            1 : "2025-04-07T14:45:00.000Z",
            2 : "2025-04-07T15:00:00.000Z"
            }
            
        value = get_valid_index_input("test :", index_validator_mock, menu)
        self.assertEqual(value, 2)