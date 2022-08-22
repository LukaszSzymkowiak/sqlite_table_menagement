import sqlite3


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

    @classmethod
    def change_table_name(cls, connection, table):
        name = input("Rename table: ")
        cursor = connection.cursor()
        cursor.execute(f"ALTER TABLE {table} RENAME {name}")


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
