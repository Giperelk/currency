from unittest.mock import MagicMock


def get_request_mocker(mocker, data):
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: data
        )
    )
    return request_get_mock
