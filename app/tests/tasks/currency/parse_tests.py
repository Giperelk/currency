from currency.tasks import parse_privatbank, parse_monobank
from currency.models import Rate

from tests.utils.task_utils import get_request_mocker
from tests.constants.currency.parse import PRIVATBANK_DATA, MONOBANK_DATA


def test_parse_privatbank(mocker):
    initial_count = Rate.objects.count()
    privat_data = PRIVATBANK_DATA
    request_get_mock = get_request_mocker(mocker, privat_data)  # noqa: F841
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2


def test_parse_monobank(mocker):
    monobank_data = MONOBANK_DATA
    initial_count = Rate.objects.count()
    request_get_mock = get_request_mocker(mocker, monobank_data)  # noqa: F841
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
