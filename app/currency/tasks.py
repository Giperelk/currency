import requests
from celery import shared_task
from currency.choices import RateCurrencyChoices
from currency.constants import (
    PRIVATBANK_CODE_NAME, PRIVATBANK_URL,
    MONOBANK_CODE_NAME, MONOBANK_URL
)
from currency.utils import to_2_point_decimal, get_or_create_source, create_rate_if_not_exist


@shared_task
def parse_privatbank():

    source = get_or_create_source(
        code_name=PRIVATBANK_CODE_NAME,
        source_url=PRIVATBANK_URL,
        name=PRIVATBANK_CODE_NAME,
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'
    response = requests.get(url=url)
    rates = response.json()

    available_currencies = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate["ccy"] not in available_currencies:
            continue

        buy = to_2_point_decimal(rate["buy"])
        sale = to_2_point_decimal(rate["sale"])
        currency = rate["ccy"]

        create_rate_if_not_exist(
            currency_code=available_currencies[currency],
            source=source,
            buy=buy,
            sale=sale,
        )


@shared_task
def parse_monobank():

    source = get_or_create_source(
        code_name=MONOBANK_CODE_NAME,
        source_url=MONOBANK_URL,
        name=MONOBANK_CODE_NAME
    )

    available_currencies = {
        'USD': {
            'choice': RateCurrencyChoices.USD,
            'numeric_code': 840,
        },
        'EUR': {
            'choice': RateCurrencyChoices.EUR,
            'numeric_code': 978,
        },
    }

    url = 'https://api.monobank.ua/bank/currency'

    response = requests.get(url=url)
    rates = response.json()

    for rate in rates:
        for currency_key, currency in available_currencies.items():
            if currency['numeric_code'] == rate['currencyCodeA']:
                buy = to_2_point_decimal(rate["rateBuy"])
                sale = to_2_point_decimal(rate["rateSell"])
                currency = currency_key

                create_rate_if_not_exist(
                    currency_code=available_currencies[currency]["choice"],
                    source=source,
                    buy=buy,
                    sale=sale,
                )


@shared_task
def parse_sources():
    parse_privatbank.delay()
    parse_monobank.delay()
