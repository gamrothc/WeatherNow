import requests

def cToFahrenheit(celsius):
    return (celsius * 1.8) + 32

def callWeatherStack(zipcode, accessKey):
    params = {
      'access_key': accessKey,
      'query': zipcode
    }

    weather_api_result = requests.get('http://api.weatherstack.com/current', params)

    api_response = weather_api_result.json()

    print(u'Current temperature in %s is %d degrees Fahrenheit' % (api_response['location']['name'], cToFahrenheit(api_response['current']['temperature'])))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    accessKey = '0b9ee0340f88066156ff8200cbd30ef0'
    zipcode = input("Enter your zipcode: ")

    if len(zipcode) == 5:
        callWeatherStack(zipcode, accessKey)
    else:
        print("Invalid Input - zipcode should be 5 numbers")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
