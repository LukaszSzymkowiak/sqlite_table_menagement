import sqlite3
from column import *


class Table:
    def __init__(self):
        self.name = "Table"

    @classmethod
    def get_tables_list(cls, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return cursor.fetchall()

    @classmethod
    def add_table(cls, connection):
        table_name = input("Table name: ")
        column_name = input("Column name: ")
        column_type = input("Column type: ")
        print()
        try:
            cursor = connection.cursor()
            cursor.execute(
                f"CREATE TABLE {table_name} ({column_name} {column_type})")
            print(f"Table {table_name} created\n")
        except sqlite3.OperationalError:
            print("Table already exist\n")

    @classmethod
    def delete_table(cls, connection):
        table_name = input(
            f"Selcet table to delete from list: {Table.get_tables_list(connection)}: ")
        print()
        try:
            cursor = connection.cursor()
            cursor.execute(f"DROP TABLE {table_name}")
            print(f"Table {table_name} deleted\n")
        except sqlite3.OperationalError:
            print("Table doesn't exist\n")

    # in progress!!!
    @classmethod
    def change_table_name(cls, connection, table):
        name = input("Rename table: ")
        cursor = connection.cursor()
        cursor.execute(f"ALTER TABLE {table} RENAME {name}")



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