def get_valid_input(input_text, validator):

    while True:
        value = input(input_text).strip()

        if validator(value):
            return value



def get_valid_index_input(input_text, validator, menu):

    while True:

        print("horários disponíveis:")
        print("-" * 50)
        for slot in menu:
            time = menu[slot].split("T")[1].split(".")[0]
            print(f"({slot}) : {time}")
        print("-" * 50)
        
        value = input(input_text).strip()

        if validator(value, menu):
            return int(value)