from database import Database
from helpers import clear_console, get_enter, get_option, get_text

class Teams:
    def __init__(self):
        self.db = Database()

    def print_all(self):
        cur = self.db.conn.cursor()

        cur.execute('''
            SELECT id, name, barcode FROM teams WHERE 1;
        ''')

        result = cur.fetchall()

        if len(result) > 0:
            print("ID \t Name \t Barcode")
            print("--- \t --- \t ---")
        else:
            print("No teams yet.")

        for (id, name, barcode) in result:
            print(f"{id} \t {name} \t {barcode}")

        return result

    def list_all(self):
        self.print_all()
        
        get_enter()

    def create(self):
        cur = self.db.conn.cursor()

        name = get_text("Enter a name for the team: ")
        barcode = 0

        try:
            cur.execute('INSERT INTO teams (NAME, BARCODE) VALUES (?, ?)', [name, barcode])
            self.db.conn.commit()

            print(f"Successfully added team '{name}'!")
        except:
            print("Cannot create team, please try again later.")

        get_enter()

    def delete(self):
        cur = self.db.conn.cursor()

        teams = self.print_all()

        tl = {id:name for (id, name, barcode) in teams}
        
        option = get_option("Enter team ID to delete: ", tl)

        try:
            cur.execute("DELETE FROM `teams` WHERE `id` = ?;", (option,))
            self.db.conn.commit()

            clear_console()
            self.print_all()

            print(f"Successfully deleted team {option}.")
        except:
            print("Cannot delete team, please try again later.")

        get_enter()
        