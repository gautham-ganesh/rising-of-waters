import pytest
from app import app


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    app.secret_key = 'test-secret'
    with app.test_client() as client:
        yield client


def test_prediction_redirects_to_result_page(client):
    response = client.post(
        '/predict',
        data={
            'temp': '30',
            'humidity': '70',
            'cloud_cover': '40',
            'annual_rainfall': '1200',
            'jan_feb': '250',
            'mar_may': '300',
            'jun_sep': '400',
            'oct_dec': '200',
            'avg_june': '150',
            'sub_index': '1.5',
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/result')

    result_response = client.get('/result')
    assert result_response.status_code == 200
    assert b'Prediction Result' in result_response.data
    assert b'Flood Probability' in result_response.data
