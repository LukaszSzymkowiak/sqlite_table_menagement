from classes import *


def table_loop(table):
    connection = sqlite3.connect("database.db")
    while True:
        print(f"Table \"{table}\"")
        user_choice = input("1 - show columns\n"
                            "2 - go to column\n"
                            "3 - add column\n"
                            "4 - delete column\n"
                            "5 - change table name - IN PROGRESS\n"
                            "0 - back\nInput: ")
        print()
        if user_choice == "0":
            break
        elif user_choice == "1":
            print(Column.show_columns(connection, table))
            print()
        elif user_choice == "2":
            column = input(f"Select column from {Column.show_columns(connection, table)}: ")
            print()
            column_loop(table, column)
        elif user_choice == "3":
            Column.add_column(connection, table)
        elif user_choice == "4":
            Column.delete_column(connection, table)
        elif user_choice == "5":
            Table.change_table_name(connection, table)
        else:
            print("Invalid command\n")


def column_loop(table, column):
    connection = sqlite3.connect("database.db")
    while True:
        print(f"Column \"{column}\" from table \"{table}\"")
        user_choice = input("1 - show column\n"
                            "2 - add row to column\n"
                            "3 - delete row from column\n"
                            "0 - back\nInput: ")
        print()
        if user_choice == "0":
            break
        elif user_choice == "1":
            Row.show_rows_from_column(connection, table, column)
        elif user_choice == "2":
            Row.add_row_to_column(connection, table, column)
        elif user_choice == "3":
            Row.delete_row_from_column(connection, table, column)
        else:
            print("Invalid command\n")
