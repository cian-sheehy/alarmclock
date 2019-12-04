from gtts import gTTS
import os
import vlc
from subprocess import call
from random import choice
from time import sleep


def make_mp3(words, mp3name, language="en"):
    # it creates an mp3 file using google API
    tts = gTTS(text=words, lang=language)
    try:
        os.remove("%s.mp3" % mp3name)
    except OSError:
        pass
    tts.save("%s.mp3" % mp3name)
    print("File %s.mp3 has been created" % mp3name)


def play_audio(audio_file):
    print("Playing {} file..".format(audio_file))
    call(["cvlc", audio_file, "--play-and-exit"])
    sleep(2)


def random_radio():
    radio_dict = {
        "BBC 1": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p",
        "Radio Active": "http://streaming.radio.co/s6ef1e80ce/listen.m3u"
        #'2 FM': 'http://icecast2.rte.ie/ie2fm',
        #'Today FM':'http://15833.live.streamtheworld.com/TODAY_FM.mp3?csegid=10'
    }

    radio_name, radio_link = choice(list(radio_dict.items()))
    print(radio_name + " has been chosen for you today.")

    return radio_name, radio_link
