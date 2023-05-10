def test_get_api_source_list_code_200(authorized_api_client):
    response = authorized_api_client.get('/api/currency/sources/')
    assert response.status_code == 200


def test_get_api_source_list_code_401(not_authorized_api_client):
    response = not_authorized_api_client.get('/api/currency/sources/')
    assert response.status_code == 401


def test_create_api_source_empty_data(authorized_api_client):
    response = authorized_api_client.post('/api/currency/sources/', )
    assert response.status_code == 400
    assert response.json() == {
        'source_url': ['This field is required.'],
        'name': ['This field is required.'],
        'code_name': ['This field is required.']
    }


def test_create_api_source_valid_data(authorized_api_client):
    payload = {
        'source_url': 'https://monobank.com.ua',
        'name': 'monobank',
        'code_name': 'monobank'
    }
    response = authorized_api_client.post('/api/currency/sources/', data=payload)
    assert response.status_code == 201


def test_put_api_source_data(authorized_api_client):
    payload = {
        'source_url': 'https://monobank.com.ua',
        'name': 'bank_name',
        'code_name': 'monobank'
    }
    response = authorized_api_client.put('/api/currency/sources/1', data=payload)
    assert response.status_code == 301
    assert response.url == '/api/currency/sources/1/'


def test_patch_api_source_valid_data(authorized_api_client):
    payload = {
        'source_url': 'https://monobank.com.ua',
        'name': 'bank_name',
    }
    response = authorized_api_client.patch('/api/currency/sources/1', data=payload)
    assert response.status_code == 301
    assert response.url == '/api/currency/sources/1/'


def test_get_details_api_source_code_200(authorized_api_client):
    response = authorized_api_client.get('/api/currency/sources/1/', )
    assert response.status_code == 200


def test_delete_details_api_source(authorized_api_client):
    response = authorized_api_client.delete('/api/currency/sources/1/')
    assert response.status_code == 204
