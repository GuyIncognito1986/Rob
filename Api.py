#API Search 
# use 3.py>output.txt to write to text
# This example only returns 1 result 
import requests
import json


def get_response(term = "any:AS186"):
    parameters = {
    "versionNumber": 1.1,
    "term": term,
    "storeInfo.id": "uk.farnell.com",
    "resultsSettings.offset": 0,
    "resultsSettings.numberOfResults": 1,
    "resultsSettings.refinements.filters": "rohsCompliant",
    "resultsSettings.responseGroup": "large",
    "callInfo.omitXmlSchema": "false",
    "callInfo.responseDataFormat": "json",
    "callinfo.apiKey": "a842zske3sx5temdsrwc6s2b"
    }

    response = requests.get("https://api.element14.com/catalog/products?", parameters)

    return response


# x = response.json()
# y = json.dumps(x, indent=4, sort_keys=True)
# print(y)

#####################

#import re
#z=re.findall("countryOfOrigin",y)
#print(z)

######################