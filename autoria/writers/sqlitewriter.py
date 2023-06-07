import sqlite3
from .abcwriter import ABCWriter


class SQLiteWriter(ABCWriter):

    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers
        self.con = sqlite3.connect(self.filename)
        self.cur = self.con.cursor()

        try:
            data = f'{headers[0]} INTEGER UNIQUE, {headers[1]}'
            self.cur.execute(f"CREATE TABLE Cars({data})")
        except sqlite3.OperationalError:
            pass

        try:
            data = f'{headers[0]} INTEGER UNIQUE, title, price, km'
            self.cur.execute(f"CREATE TABLE Cardetails({data})")
        except sqlite3.OperationalError:
            pass

    def write(self, row: tuple):

        data = f"{row[0]}, '{row[1]}'"

        self.cur.execute(f"INSERT OR IGNORE INTO Cars VALUES ({data})")

        self.con.commit()

    def __del__(self):
        self.con.close()

    def write_detail(self, row: tuple):
        data = f"{row[0]}, '{row[1]}', '{row[2]}', '{row[3]}'"

        self.cur.execute(f"INSERT OR IGNORE INTO Cardetails VALUES ({data})")

        self.con.commit()


if __name__ == '__main__':
    sqlwriter = SQLiteWriter('tutorial.db', ['car_id', 'data_link_to_view'])


