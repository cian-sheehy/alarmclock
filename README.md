# alarmclock
Python based alarmclock for Raspberry Pi 3

## Prereqresities

### Installation
* Install gTTS `python3 -m pip install request`
* Install request `python3 -m pip install gtts`
* Install vlc `python3 -m pip install python-vlc`
* Install praw `python3 -m pip install praw`

### Reddit Account Setup
* Create an app here with name `bot` and redirect url `http://127.0.0.1`. When you click create app you'll see the id and secret
    `https://old.reddit.com/prefs/apps/`
* You will need to create a praw.ini file which holds your reddit id and key
    `https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html`

## Run the alarm
* `python3 alarmclock.py`