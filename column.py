import sqlite3
from row import *


class Column:
    def __init__(self):
        self.name = "Column"

    @classmethod
    def show_columns(cls, connection, table):
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({table})")
        return cursor.fetchall()

    @classmethod
    def add_column(cls, connection, table):
        column = input("Column name: ")
        type = input("Column type: ")
        print()
        try:
            cursor = connection.cursor()
            cursor.execute(
                f"ALTER TABLE {table} ADD {column} {type}")
            print(f"\nColumn: {column} created in table: {table}\n")
        except sqlite3.OperationalError:
            print("Table doesn't exist\n")

    @classmethod
    def delete_column(cls, connection, table):
        column = input("Column name: ")
        print()
        try:
            cursor = connection.cursor()
            cursor.execute(
                f"ALTER TABLE {table} DROP COLUMN {column}")
            print(f"\nColumn: {column} deleted from table: {table}\n")
        except sqlite3.OperationalError:
            print("Table doesn't exist\n")


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