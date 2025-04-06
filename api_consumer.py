import requests
import os
from dotenv import load_dotenv


load_dotenv()
class Scheduling:

    def __init__(self):
        self.username = os.environ.get("USER_NAME")
        self.auth = {"Authorization": os.environ.get("API_KEY")}
        self.slots_menu = {}


    def get_avaliable_slots(self, date):

        headers = {
            "cal-api-version": "2024-09-04"
        } | self.auth

        params = {
            "eventTypeSlug" : "reuniao",
            "username" : self.username,
            "start" : date,
            "end" : date,
            "timeZone" : "America/Sao_Paulo"
        }

        url = "https://api.cal.com/v2/slots"
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()["data"].get(date, [])

        else: 
            print("Error : ", response.text)
    
    def show_slots(self, slots):
        print("Horarios disponiveis: ")

        print()
        for index, slot in enumerate(slots):
            self.slots_menu[index] = slot['start']

            time = str(self.slots_menu[index])
            time = time.split("T")[1].split(".")[0]

            print(f"({index}) = {time}")
        print()

    
    def booking(self, selected, name, email ):
        url = "https://api.cal.com/v2/bookings"

        headers = {
            "cal-api-version": "2024-08-13",
            "Content-Type" : "application/json"
        }  | self.auth

        payload = {
            "eventTypeId": 2208568,
            'start': self.slots_menu[selected],
            "attendee" : {
                "timeZone" : "America/Sao_Paulo",
                "email" : email,
                "name" : name 
            }   
        }

        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code >= 200 and response.status_code <= 299:
            print("Horario agendado com sucesso!")
        else:
            print(f"Error {response.status_code}: {response.text}")