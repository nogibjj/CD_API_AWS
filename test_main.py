"""import testclient for testing"""
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)


def test_root():
    """test root"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, this is a text preposessing api"}


def test_request_no_params():
    """test 422 status"""
    response = response = client.get("/preprocess/")
    assert response.status_code == 422


def test_replace_phone():
    """test phone number"""
    data = {
        "text": "Hello, my name is Jojo, I'm 21. My phone Number is +1 984377-9168",
        "steps": ["replace_phone"],
    }
    response = client.get("/preprocess/", json=data)
    assert response.status_code == 200
    # print(response.json())
    assert response.json() == {
        "steps": ["replace_phone"],
        "text": "Hello, my name is Jojo, I'm 21. My phone Number is +1 984377-9168",
        "preprocessed_text": "Hello, my name is Jojo, I'm 21. My phone Number is  <PHONE_NUMBER> ",
    }


def test_replace_num():
    """test replace number"""
    data = {
        "text": "Hello, my name is Jojo, I'm 21. My phone Number is +1 984377-9168",
        "steps": ["replace_number_like"],
    }
    response = client.get("/preprocess/", json=data)
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {
        "steps": ["replace_number_like"],
        "text": "Hello, my name is Jojo, I'm 21. My phone Number is +1 984377-9168",
        "preprocessed_text": "Hello, my name is Jojo, I'm  <NUMERIC_VALUE>  My phone Number is + <NUMERIC_VALUE> ",
    }


if __name__ == "__main__":
    test_request_no_params()
    test_replace_num()
