import requests

# Get API without parameter
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# iss_position = data["iss_position"]
# latitude = iss_position["latitude"]
# longitude = iss_position["longitude"]
# print(latitude)
# print(longitude)

# Get API with parameters

MY_LAT = -3.318607
MY_LONGITUDE = 114.594376

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)

# Get sunrise hour and sunset hour
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour)
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunset_hour)
