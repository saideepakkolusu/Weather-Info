import requests
import json


City=input("Enter the name of the city:")
## WE CAN GET FREE WEATHER API IN WETHERAPI.COM
url=f"http://api.weatherapi.com/v1/current.json?key=2bfb1aff759f409db4c111656251607&q={City}"

r = requests.get(url)

wdic=json.loads(r.text)

print(wdic["location"]["region"])
print(wdic["current"]["temp_c"])
print(wdic["current"]["condition"]["text"])

