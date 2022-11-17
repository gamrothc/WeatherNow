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

    return weather_api_response['location']['name'], cToFahrenheit(weather_api_response['current']['temperature'])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Weatherstack
    # weatherstack_accessKey = '0b9ee0340f88066156ff8200cbd30ef0'
    weatherstack_access_key = os.environ['WEATHERSTACK_ACCESS_KEY']
    zipcode = input("Enter your zipcode: ")
    phonenumber = input("Enter your phone number (include '+1'): ")

    if len(zipcode) == 5:
        city, temperature = callWeatherStack(zipcode, weatherstack_access_key)
    else:
        print("Invalid Input - zipcode should be 5 numbers")
    
    #Set Twilio Credentials
    twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(twilio_account_sid, twilio_auth_token)

    # Formulate and Send Weather Report
    weather_message = "Current temperature in " + str(city) + " is " + str(temperature) + " degrees Fahrenheit."
    message = client.messages.create(
        body=weather_message,
        from_='+14254753954',
        to=phonenumber
    )

    print(message.sid) #onlt here for testing, can be removed eventually
