# WeatherNow
WeatherNow application to get weather data and send text message to users 

# Before Running
The code relies on using our API access tokens. For security purposes, we stored our tokens in our environment variables and retrieve them using Python’s ‘os’ library so that they were not displayed directly on Github. If you would like our access tokens, please reach out to our team.

# To Run
In the terminal run command: 'py main.py' ***Note: Some users run python scripts from their terminal using 'python' or 'python3'. Replace 'py' with whatver your computer uses.***

You will be prompted to enter a zip code, followed by a phone number. The program will then send a weather report to that phone number. ***Note: We use a free Twilio subscription and can only send texts to an approved list of phone numbers. If you would like us to add your number to our approved list, please reach out to our team.***
