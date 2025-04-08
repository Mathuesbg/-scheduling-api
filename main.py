from api_consumer import Scheduling
from validators import name_is_valid, email_is_valid, date_is_valid, index_is_valid
                        

from utils.input_helpers import get_valid_input, get_valid_index_input

def main():
    print("Sistema de agendamento")

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

    index = get_valid_index_input("Escolha um horario a partir do indice: ", index_is_valid, menu)


    result = schedule.booking(index, name, email)
    print(result)

if __name__ == "__main__":
    main()