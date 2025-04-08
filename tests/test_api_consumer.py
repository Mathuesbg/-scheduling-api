from unittest import TestCase
import api_consumer
from unittest.mock import patch

class ApiConsumerTest(TestCase):

    @patch("api_consumer.requests.get")
    def test_get_avaliable_slots_returns_a_list(self, mock_get):
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data" : {"2025-04-07" : [
                {"start" : "2025-04-07T10:00:00.000Z"},
                {"start" : "2025-04-07T12:00:00.000Z"}
                ]
            }
        } 

        date = "2025-04-07"
        scheduler = api_consumer.Scheduling()
        response = scheduler.get_avaliable_slots(date)
        
        self.assertIsInstance(response, list, "Response should be a list")

    @patch("api_consumer.requests.get")
    def test_get_avaliable_slots_returns_a_list_of_dicts(self, mock_get):
        date = "2025-04-07"

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data" : {"2025-04-07" : [
                {"start" : "2025-04-07T10:00:00.000Z"},
                {"start" : "2025-04-07T12:00:00.000Z"}
                ]
            }
        }  

        
        scheduler = api_consumer.Scheduling()
        response = scheduler.get_avaliable_slots(date)
        
        for slot in response:
            self.assertIsInstance(slot, dict, "Each slot should be a dictionary")


    @patch("api_consumer.requests.get")
    def test_get_avaliable_slots_error(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = "Not Found"

        scheduler = api_consumer.Scheduling()
        date = "2025-04-07"
        response = scheduler.get_avaliable_slots(date)

        self.assertEqual(response[0], 404)
        self.assertEqual(response[1], "Not Found")

    def test_get_slots_menu_retuns_menu_correctly(self):

        slots = [
            {"start" : "2025-04-07T10:00:00.000Z"},
            {"start" : "2025-04-07T12:00:00.000Z"},
            {"start" : "2025-04-07T14:00:00.000Z"},
            ]

        scheduler = api_consumer.Scheduling()
        menu = scheduler.get_slots_menu(slots)

        self.assertEqual(menu.get(0), "2025-04-07T10:00:00.000Z")
        self.assertEqual(len(menu), 3)
        self.assertIsInstance(menu, dict)

    @patch("api_consumer.requests.post")
    def test_booking_return_booking_confirmed(self, mock_post):

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = "OK"

        name = "User"
        email = "user@mail.com"
        selected = 1

        scheduler = api_consumer.Scheduling()

        scheduler._Scheduling__slots_menu = {
            1: "2025-04-07T14:30:00.000Z"
        }

        result = scheduler.booking(selected, name, email)

        self.assertEqual(result, "Horario agendado com sucesso! 200")

    @patch("api_consumer.requests.post")
    def test_booking_return_booking_error(self, mock_post):

        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad Request"


        name = "User"
        email = "user@mail.com"
        selected = 1

        scheduler = api_consumer.Scheduling()

        scheduler._Scheduling__slots_menu = {
            1: "2025-04-07T14:30:00.000Z"
        }

        result = scheduler.booking(selected, name, email)

        self.assertEqual(result, "Error : 400")

        
