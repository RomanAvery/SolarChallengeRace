import sqlite3
import os

from helpers import clear_console, get_option
from teams import Teams
tm = Teams()

running = True

def handle_menu():
    global running

    menu_options = {
        1: 'List teams',
        2: 'Add a team',
        3: 'Delete a team',
        4: 'Create a barcode',
        5: 'List races',
        6: 'Add a race',
        7: 'Delete a race',
        8: 'Run a race',
        99: 'Exit'
    }

    clear_console()

    print(f"---Welcome to the Solar Challenge---")

    for key in menu_options.keys():
        print(f"{key}) {menu_options[key]}")

    option = get_option("Enter your choice: ", menu_options)

    clear_console()

    if option == 1:
        tm.list_all()
    elif option == 2:
        tm.create()
    elif option == 3:
        tm.delete()
    elif option == 4:
        pass
    elif option == 99:
        running = False
    

def main():
    while running:
        handle_menu()

# Main function
if __name__ == "__main__":
    main()
