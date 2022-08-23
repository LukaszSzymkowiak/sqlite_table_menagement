import sqlite3


class Row:
    def __init__(self):
        self.name = "Row"

    @classmethod
    def add_row_to_column(cls, connection, table, column):
        user_choice = input("Add to column: ")
        print()
        try:
            cur = connection.cursor()
            cur.execute(
                f"INSERT INTO {table}({column}) VALUES(?)", (user_choice,))
            connection.commit()
            print(f"{user_choice} added to table: {table}, column: {column}")
            print()
        except sqlite3.OperationalError:
            print("table or column or item doesn't exist\n")

    @classmethod
    def delete_row_from_column(cls, connection, table, column):
        choice = input("Delete from column: ")
        print()
        try:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM {table} WHERE {column} = ?", (choice,))
            connection.commit()
            print(f"{choice} deleted from table: {table}, column: {column}")
            print()
        except sqlite3.OperationalError:
            print("table or column or item doesn't exist\n")

    @classmethod
    def show_rows_from_column(cls, connection, table, column):
        print()
        try:
            cur = connection.cursor()
            cur.execute(f"SELECT rowid, {column} FROM {table}")
            results = cur.fetchall()
            for result in results:
                print(f"{result[0]}. {result[1]}")
            print()
        except sqlite3.OperationalError:
            print("table or column or item doesn't exist\n")
