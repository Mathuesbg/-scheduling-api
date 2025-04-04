import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

headers = {
    "Authorization": os.environ.get("API_KEY"),
    "cal-api-version": "2024-09-04"
}

USERNAME = os.environ.get("USER_NAME")
endpoint = f"https://api.cal.com//v2/slots"
query_string = f"?eventTypeSlug=reuniao&username={USERNAME}&start=2025-04-05&end=2025-04-07&timeZone=America/Sao_Paulo"

url = endpoint + query_string

response = requests.get(url, headers=headers)
dates = response.json()["data"]

menu = {}

print("Horarios disponiveis: ")
print()

for day in dates:

    for index, slot in enumerate(dates[day]):
        menu[index] = slot['start']
        print(f"({index}) = {menu[index]}")

print()
selected = int(input("Escolha um horario a partir do indice: "))
name = input("Digite seu nome: ")
email = input("Digite seu email: ")


url = "https://api.cal.com/v2/bookings"

headers = {
    "Authorization": os.environ.get("API_KEY"),
    "cal-api-version": "2024-08-13",
    "Content-Type" : "application/json"

}

payload = {
    "eventTypeId": 2208568,
    'start': menu[selected],
    "attendee" : {
        "timeZone" : "America/Sao_Paulo",
        "email" : email,
        "name" : name 
    }   
}   

response = requests.post(url, json=payload, headers=headers)