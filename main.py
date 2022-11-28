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

    return weather_api_response['location']['name'], cToFahrenheit(weather_api_response['current']['temperature']), \
            cToFahrenheit(weather_api_response['current']['feelslike']), weather_api_response['current']['uv_index'], \
            weather_api_response['current']['precip']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    weatherstack_access_key = os.environ['WEATHERSTACK_ACCESS_KEY']
    twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

    zipcode = input("Enter your zipcode: ")
    phonenumber = input("Enter your phone number: ")

    if len(zipcode) == 5:
        city, temperature, feels_like, uv_index, rain = callWeatherStack(zipcode, weatherstack_access_key)
    else:
        print("Invalid Input - zipcode should be 5 numbers")
 
    client = Client(twilio_account_sid, twilio_auth_token)

    # Formulate and Send Weather Report
    weather_message = "Current temperature in " + str(city) + " is " + str(temperature) + " degrees Fahrenheit " \
                    "with a real-feel of " + str(feels_like) + " degrees Fahrenheit. The UV Index is " + str(uv_index) + "."
    message = client.messages.create(
        body=weather_message,
        from_='+14254753954',
        to=phonenumber
    )

    print(message.sid)  # only here for testing, can be removed eventually
