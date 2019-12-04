import urllib.request
import datetime
import json
from pprint import pprint
import os
import pytz
import audio
from news import getNews


def data_fetch():
    url = urllib.request.urlopen(
        "http://api.openweathermap.org/data/2.5/weather?q=Wellington,NZ&appid=eebff5080fe465f502a74bcbd2805989"
    )
    raw_api_dict = json.loads(url.read().decode("utf-8"))
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        current_time=current_time(),
        city=raw_api_dict.get("name"),
        temp=temp_converter(raw_api_dict.get("main").get("temp")),
        temp_max=temp_converter(raw_api_dict.get("main").get("temp_max")),
        temp_min=temp_converter(raw_api_dict.get("main").get("temp_min")),
        sky=raw_api_dict["weather"][0]["main"],
        sky_desc=raw_api_dict["weather"][0]["description"],
    )
    return data


def set_text(data):
    opening = (
        "Wake up Cian, it's {} . The sky is {} with current temperature {} . Here are some top headlines for today."
    ).format(str(data["current_time"]), str(data["sky"]), str(data["temp"]),)

    return opening + getNews()


def main(text):
    mp3_file = "alarm_clock"
    print("Writing to {}.mp3 file..".format(mp3_file))

    radio_nm, radio_link = audio.random_radio()

    text += "\nFinally, " + radio_nm + " radio.."
    audio.make_mp3(text, mp3_file)

    audio.play_audio("%s.mp3" % mp3_file)
    audio.play_audio(radio_link)


def current_time():
    current_time = (
        datetime.datetime.utcnow()
        .replace(tzinfo=pytz.utc)
        .astimezone(pytz.timezone("Pacific/Auckland"))
        .strftime("%H:%M %p")
    )
    return current_time


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime("%H:%M %p")
    return converted_time


def temp_converter(temperature):
    converted_temp = temperature - (273.15)
    return int(round(converted_temp))


if __name__ == "__main__":
    main(set_text(data_organizer(data_fetch())))
