from api_consumer import Scheduling
from validators import name_is_valid, email_is_valid, date_is_valid, get_valid_input, selected_is_valid, get_valid_index_input


name = get_valid_input("Digite seu nome: ", name_is_valid)
email = get_valid_input("Digite seu email: ", email_is_valid)
date = get_valid_input("Digite a data em que deseja agendar (YYYY-MM-DD): ", date_is_valid)

schedule = Scheduling()
slots = schedule.get_avaliable_slots(date)

while not slots : 
    print(f"Não há horários diponiveis para o dia {date}")

    date = get_valid_input("Digite a data em que deseja agendar (YYYY-MM-DD): ", date_is_valid)
    slots = schedule.get_avaliable_slots(date)

menu = schedule.get_slots_menu(slots)

selected = get_valid_index_input("Escolha um horario a partir do indice: ", selected_is_valid, menu)


result = schedule.booking(selected, name, email)
print(result)
