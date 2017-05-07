# chromeline

Live stream line in on a Pi to a Chromecast.

## Setup on Pi

First:

    chmod 755 install_prerequisites.sh
    ./install_prerequisites.sh

Then hook up some magic:

    gconftool-2 -t string --set /system/gstreamer/0.10/default/audiosrc pulsesrc

Allow scripts to execute:

    chmod 755 push_to_icecast.sh

### Icecast configuration

Edit /etc/icecast2/icecast.xml

Change:

    burst-on-connect = 0
    burst-size = 0

Then:

    sudo /etc/init.d/icecast2 restart

### Input device name

Need to know your input sound card name for the config:

    pactl list

Then update the config.ini with it (and the other settings you'll need).

## Starting chromeline

For now, this will be a daemon later:

    sudo pip install virtualenv
    virtualenv venv
    source venv/bin/activate

    pip install -r requirements.txt
    python chromeline.py

As soon as the desired Chromecast is detected, line in will be streamed to it.

For auto-starting for now, I am doing (in crontab):

    @reboot cd /home/pi/chromeline ; venv/bin/python chromeline.py
