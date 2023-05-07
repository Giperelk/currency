def test_get_api_rate_list_code_200(authorized_api_client):
    response = authorized_api_client.get('/api/currency/rates/')
    assert response.status_code == 200


def test_get_api_rate_list_code_401(not_authorized_api_client):
    response = not_authorized_api_client.get('/api/currency/rates/')
    assert response.status_code == 401


def test_create_rate(authorized_api_client):
    payload = {
        'buy': 10,
        'sale': 20,
        'source': 1,
    }
    response = authorized_api_client.post('/api/currency/rates/', data=payload)
    assert response.status_code == 201
