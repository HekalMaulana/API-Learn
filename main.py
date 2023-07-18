import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_position = data["iss_position"]
latitude = iss_position["latitude"]
longitude = iss_position["longitude"]
print(latitude)
print(longitude)
