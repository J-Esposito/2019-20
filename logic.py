import datetime
import requests

opt_level_to_maintain = 10
base_level_to_maintain = 10

def get_weather():
    response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=4501018&APPID=66387745b51f3f23fbc5412ce292097f")
    
    return response.json()

def evaluate_logic(weather_data,water_level):

    day = datetime.datetime.today().weekday()
    amt_rain = weather_data[day]
    if amt_rain > 0:
        if water_level < base_level_to_maintain:
            return True
        else:
            return False
    else:
        if water_level < opt_level_to_maintain:
            return True
        else:
            return False
            
def sum_rain(weather_data):
    days = [0,0,0,0,0]
    for i in range(len(weather_data["list"])):
        print(i)
        if "rain" in weather_data["list"][i].keys() and "3h" in weather_data["list"][i]["rain"].keys():
            days[int(i/8)] += weather_data["list"][i]["rain"]["3h"]
    return days
            
print(sum_rain(get_weather()))