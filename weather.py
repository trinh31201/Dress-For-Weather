import requests

def fetchForecast(location, apikey):
    url = "https://api.tomorrow.io/v4/timelines"

    params = {
        "apikey": apikey,
        "location": location,
        "fields": "temperature,temperatureApparent,weatherCode",
        "units": "metric",
        "timesteps": "1h",
        "startTime": "now",
        "endTime": "nowPlus6h",
        "timezone": "Japan"
    }

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip"
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()
    data = data['data']['timelines'][0]['intervals']
    print(data)
    return data
def consumeOne(forecast):
    return {
        "temp": forecast['values']['temperature'],
        "feel": forecast['values']['temperatureApparent'],
        "weather_code": forecast['values']['weatherCode']
        }

def consumeForecasts(forecasts):
    parsed_forecasts = list(map(consumeOne, forecasts))
    mintemp = min(list(map(lambda f: f["temp"], parsed_forecasts)))
    maxtemp = max(list(map(lambda f: f["temp"], parsed_forecasts)))
              
    minfeel = min(list(map(lambda f: f["feel"], parsed_forecasts)))
    maxfeel = max(list(map(lambda f: f["feel"], parsed_forecasts)))


    
    is_sunny = any(list(map(lambda f: f["weather_code"] in [1000,1100,1101], parsed_forecasts)))
    is_rainy = any(list(map(lambda f: f["weather_code"] in [4000,4001,4200,4201], parsed_forecasts)))
    is_snowy = any(list(map(lambda f: f["weather_code"] in [5000,5001,5100,5101], parsed_forecasts)))

    return {
        "mintemp": mintemp,
        "maxtemp": maxtemp,

        "minfeel": minfeel,
        "maxfeel": maxfeel,

        "is_sunny": is_sunny,
        "is_rainy": is_rainy,
        "is_snowy": is_snowy,
    }
def clothing(inp):
    umbrella = inp["is_rainy"] or inp["is_snowy"]
    sunscreen = inp["is_sunny"]
    top = None # Not set yet

    min_temp = min(inp["mintemp"], inp["minfeel"])
    max_temp = max(inp["maxtemp"], inp["maxfeel"])

    if min_temp > 15:
        if max_temp< 25:
            top = "T-Shirt"
        else:
            top = "Tank Top"
    elif max_temp < 5:
        if min_temp > -10:
            top = "Long Sleeves + Coat"
        else:
            top = "Long Sleeves + Sweater"
    else:
        if (max_temp-min_temp)> 10:
            top = "Long Sleeves + Jacket"
        else:
            top = "Long Sleeves"

    return {
            "top": top,
            "sunscreen": sunscreen,
            "umbrella": umbrella
            }

#print(clothing(consumeForecasts(fetchForecast("37.524069"+','+"139.939348", "3SwqdYkk4ONYCLHs1vS7phS9G7oehSin"))))
print(clothing(consumeForecasts(fetchForecast("LAT"+','+"LON", "APIKEY")))
