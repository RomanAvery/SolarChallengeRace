import os

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def get_option(msg, options):
    option = None
    
    while option is None:
        try:
            option = int(input(msg))
            
            if option not in options.keys():
                print('Not a valid option. Please try again.\n')
                option = None
        except:
            print('Wrong input. Please enter a number.\n')

    return option

def get_text(msg):
    text = None

    while text is None:
        try:
            text = input(msg)
        except:
            print('Wrong input. Please enter a string.\n')

    return text

def get_enter():
    input("\nPress enter to go back.")