from classes import *
from functions import *


def main():
    connection = sqlite3.connect("database.db")
    while True:
        print("DATABASE")
        user_choice = input("1 - show tables\n"
                            "2 - go to table\n"
                            "3 - add table\n"
                            "4 - delete table\n"
                            "0 - quit\nInput: ")
        print()
        if user_choice == "0":
            break
        elif user_choice == "1":
            print(f"Tables in database: {Table.get_tables_list(connection)}")
            print()
        elif user_choice == "2":
            table = input(f"Select table from list: {Table.get_tables_list(connection)}: ")
            cursor = connection.cursor()
            print()
            table_loop(table)
        elif user_choice == "3":
            Table.add_table(connection)
        elif user_choice == "4":
            Table.delete_table(connection)
        else:
            print("Invalid command\n")
    connection.close()


if __name__ == "__main__":
    main()