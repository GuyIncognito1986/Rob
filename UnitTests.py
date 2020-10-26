from Api import get_response

def test_api():
    response = get_response()
    productsArray = response['keywordSearchReturn']['products']
    countriesOfOrigin = []

    for p in productsArray:
        countriesOfOrigin.append(p['countryOfOrigin'])

    assert countriesOfOrigin[0] == 'MY'


if __name__ == "__main__":
    test_api()