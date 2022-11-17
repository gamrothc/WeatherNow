import requests
import os
from twilio.rest import Client

def cToFahrenheit(celsius):
    return (celsius * 1.8) + 32

def callWeatherStack(zipcode, accessKey):
    params = {
      'access_key': accessKey,
      'query': zipcode
    }

    weather_api_result = requests.get('http://api.weatherstack.com/current', params)

    weather_api_response = weather_api_result.json()

    print(u'Current temperature in %s is %d degrees Fahrenheit' % (weather_api_response['location']['name'], cToFahrenheit(weather_api_response['current']['temperature'])))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Weatherstack
    weatherstack_accessKey = '0b9ee0340f88066156ff8200cbd30ef0'
    zipcode = input("Enter your zipcode: ")
    
    #Twilio
    twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        body='Hi there',
        from_='+14254753954',
        to='+12016614032'
    )

    print(message.sid) 

    if len(zipcode) == 5:
        callWeatherStack(zipcode, weatherstack_accessKey)
    else:
        print("Invalid Input - zipcode should be 5 numbers")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
