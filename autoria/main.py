from writers.sqlitewriter import SQLiteWriter
from writers.csvwriter import CSVWriter
from scrappers.autoriascrapper import AutoRiaScrapper


def main():
    sql_writer = SQLiteWriter('cars.sqlite3', ['car_id', 'data_link_to_view'])
    info_writers = (
        CSVWriter('cars.csv', ['car_id', 'data_link_to_view']),
        sql_writer
    )
    detail_writers = (
        CSVWriter('car_details.csv', ['car_id', 'title', 'price', 'km']),
        sql_writer
    )

    aus = AutoRiaScrapper()
    info_list = aus.get_info(page=25850, size=10)
    for ar_id, url in info_list[-2:-1]:
        title, price, km = aus.get_details(url)
        for writer in info_writers:
            writer.write((ar_id, url))
        for writer in detail_writers:
            writer.write_detail((ar_id, title, price, km))




if __name__ == '__main__':
    main()
