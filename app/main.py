#!/usr/bin/env python3

from enum import Enum
from fastapi import FastAPI, Response, status
import json
import requests 
import os

app = FastAPI()
token = os.getenv('DISCORD_TOKEN')
channel_id = os.getenv('DISCORD_CHANNEL_ID')
url = "https://discord.com/api/webhooks/" + channel_id + "/" + token

class Condition(str, Enum):
    sunny = "sunny"
    snowy = "snowy"
    rainy = "rainy"
    windy = "windy"

def get_temp_statement(temp):
    if (temp < 0):
        return "is really cold! I would reccommend keeping your butt inside where it is nice and warm. But if you have to go out, make sure you bundle up!"
    elif (temp < 32):
        return "is quite cold. Make sure you wear long sleeves and pants honey! And don't forget a warm coat."
    elif (temp < 50):
        return "is a little chilly. I suggest a long sleeve shirt, and a pair of pants. You may be able to go without a jacket, but please stay warm dear."
    elif (temp < 72):
        return "is very pleasant. I would suggest a long sleeve shirt and some shorts sweetheart, but if you feel you'll get too hot, just switch to a t-shit!"
    elif (temp < 90):
        return "is getting a little hot. If you wear a short sleeved shirt and shorts you should be right as rain!"
    else:
        return "is really really hot! Please make sure you drink plenty of water, and don't dress too heavily. A tanktop and shorts should suffice!"

def get_condition_statement(condition):
    if (condition == Condition.sunny):
        return "so maybe a hat would be a good idea?"
    elif (condition == Condition.snowy):
        return "so make sure whatever jacket you bring is super snug and warm!"
    elif (condition == Condition.rainy):
        return "so please bring a rain jacket or an umbrella to keep you from getting soaked."
    elif (condition == Condition.windy):
        return "so a windbreaker might keep you a little warmer."

@app.get("/weather/{temperature}/{condition}")
def weather(temperature: int, condition: Condition, response: Response):
    weather_condition = get_condition_statement(condition)
    weather_temperature = get_temp_statement(temperature)
    content = str(temperature) + " " + weather_temperature + " I also see that it is " + condition +  " " + weather_condition 
    

    data = {
        "content": content,
        "username": "Mom",
        "avatar_url": "http://clipart-library.com/img1/1335115.jpg"
     }
    
    discord_response = requests.post(url, json = data)
    if (discord_response.ok == False):
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return{"message":"Looks like something went wrong"}
    return{"message":"Your message has been sent"}


