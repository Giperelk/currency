import requests
from bs4 import BeautifulSoup


class AutoRiaScrapper:

    BASE_URL = 'https://auto.ria.com/uk'

    @staticmethod
    def _get(endpoint, query_parameters):
        url = AutoRiaScrapper.BASE_URL + endpoint
        response = requests.get(url, params=query_parameters)
        response.raise_for_status()
        return response.text

    @staticmethod
    def _get_info_page_content(page: int, size: int = 100) -> str:
        query_parameters = {
            'indexName': 'auto,order_auto,newauto_search',
            'country.import.usa.not': '-1',
            'price.currency': '1',
            'abroad.not': '-1',
            'custom.not': '-1',
            'page': page,
            'size': size
        }
        endpoint = '/search'
        return AutoRiaScrapper._get(endpoint=endpoint, query_parameters=query_parameters)

    @staticmethod
    def _get_detail_page_content(url: str) -> str:
        query_parameters = {}
        return AutoRiaScrapper._get(endpoint=url, query_parameters=query_parameters)

    @staticmethod
    def get_details(url):
        page_content = AutoRiaScrapper._get_detail_page_content(url=url)
        soup = BeautifulSoup(page_content, features="html.parser")
        m_padding = soup.find("div", {"class": "m-padding"})
        title = m_padding.find("h3", {"class": "auto-content_title"}).contents[0]
        price = m_padding.find("span", {"class": "price_value"}).find("strong", {"class": ""}).contents[0]
        km = m_padding.find("div", {"class": "bold dhide"}).contents[0]
        return title, price, km

    @staticmethod
    def get_info(page: int, size: int = 100):
        result = []
        while True:
            page_content = AutoRiaScrapper._get_info_page_content(page, size)
            soup = BeautifulSoup(page_content, features="html.parser")

            page += 1

            search_results = soup.find("div", {"id": "searchResults"})
            ticket_items = search_results.find_all("section", {"class": "ticket-item"})

            if not ticket_items:
                break

            for ticket_item in ticket_items:
                car_details = ticket_item.find("div", {"class": "hide"})
                car_id = car_details['data-id']
                data_link_to_view = car_details['data-link-to-view']

                result.append((car_id, data_link_to_view))

        return result
