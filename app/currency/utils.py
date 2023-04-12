from decimal import Decimal


def to_2_point_decimal(value: str) -> Decimal:
    return round(Decimal(value), 2)


def get_or_create_source(code_name, source_url, name, logo=None):
    from currency.models import Source

    source, _ = Source.objects.get_or_create(
        code_name=code_name,
        defaults={
            'name': code_name,
            'source_url': source_url,
            'logo': logo,
        }
    )
    return source


def create_rate_if_not_exist(currency_code, source, buy, sale):
    from currency.models import Rate

    last_rate = Rate.objects.filter(
        currency=currency_code,
        source=source,
    ).order_by('created').last()

    if last_rate is not None:
        if last_rate.buy == buy or last_rate.sale == sale:
            return

    Rate.objects.create(
        buy=buy,
        sale=sale,
        currency=currency_code,
        source=source,
    )
