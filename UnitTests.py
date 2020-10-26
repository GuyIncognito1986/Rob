from Api import get_response

def test_api():
    response = get_response()
    assert response.status_code == 200


if __name__ == "__main__":
    response = get_response()
    print(response.text)