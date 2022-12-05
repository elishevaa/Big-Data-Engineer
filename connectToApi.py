

import requests
from requests.structures import CaseInsensitiveDict
# headers = {
#     'key': "b8hpP7CMOGOSgckAbOClgM0BMXUTD0kS",
#     'secret': "7ZBnFA7J4Hv9hRGG",
#     'Token':"vNrIgAZGCtF4UXzZ7s0fuUw3OeN9"
#     }
#created

headers = {
      'client_id': "b8hpP7CMOGOSgckAbOClgM0BMXUTD0kS",
      'client_secret': "7ZBnFA7J4Hv9hRGG",
    }

# get token
url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
data = "grant_type=client_credentials&client_id=N2Aq2ZZp1dCoIq0dWhRFqvcIXHcMtSD0&client_secret=gtX9KeZ9Xy6CHG3N"
resp = requests.post(url, headers=headers, data=data)
respj = resp.json()
token = respj['access_token']
print("Amadeus Token: ",token)
print(respj)
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer {}".format(token)

#get hotel by Id
hotelIds="ACPAR419"
url = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-hotels?hotelIds=ACPAR419"
resp = requests.get(url, headers=headers)
print(resp)

#get hotel By city
cityCode = "PAR"
radius="5"
radiusUnit="KM"
url = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=LON"
resp = requests.get(url, headers=headers)
print(resp)



YOUR_ACCESS_KEY="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiYWM3OGMyMWRmYmM2ZWQzOTQ0YTRjZGUyMjNiZjI2MmUzZjRjNTMwMmJkYzRiMzVjYmMxNjJmZDc2ZjMyYmJhNzUzZTY2YmFlY2UxN2U2ODAiLCJpYXQiOjE2NzAxNzMwODQsIm5iZiI6MTY3MDE3MzA4NCwiZXhwIjoxNzAxNzA5MDg0LCJzdWIiOiIxOTEwMCIsInNjb3BlcyI6W119.wzEqjN-ACukpzhjI4NX36KPY8imAH54q4ZIqSYFhItAt3FvcGdSVbZd1ZFugMELsXNYqvJAWEj-6_1I6O_EEOQ"
city="buenos aires"
country="berlin"
# get code Airport
#url="https://app.goflightlabs.com/get-airport-data?access_key={}&query=tlv".format(YOUR_ACCESS_KEY)

#get code by countries
url="https://app.goflightlabs.com/countries?access_key={}&query={}".format(YOUR_ACCESS_KEY,country)
#get  code  by city
#url="https://app.goflightlabs.com/cities?access_key={}&search={}".format(YOUR_ACCESS_KEY,city)

resp = requests.get(url)
print(resp.json())


