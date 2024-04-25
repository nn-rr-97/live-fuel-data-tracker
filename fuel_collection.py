import requests


# first step is to request to access the API
def request_access():

    url = "https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken"

    querystring = {"grant_type":"<SOME_STRING_VALUE>"}

    headers = {
        'content-type': "application/json",
        'authorization': "<SOME_STRING_VALUE>"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    # request for the fule data

    import requests


def request_fuel_data():
    url = "https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices/location"

    payload = "{\"fueltype\":\"\",\"brand\":[],\"namedlocation\":\"\",\"referencepoint\":{\"latitude\":\"\",\"longitude\":\"\"},\"sortby\":\"\",\"sortascending\":\"\"}"
    headers = {
        'content-type': "<SOME_STRING_VALUE>",
        'authorization': "<SOME_STRING_VALUE>",
        'apikey': "<SOME_STRING_VALUE>",
        'transactionid': "<SOME_STRING_VALUE>",
        'requesttimestamp': "<SOME_STRING_VALUE>"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return