# chromeline

Live stream line in on a Pi to a Chromecast.

## Setup on Pi

First:

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

## Input device name

Need to know your input sound card name for the config:

    pactl list

## Starting chromeline

For now, this will be a daemon later:

    sudo pip install virtualenv
    virtualenv venv
    source venv/bin/activate

    pip install -r requirements.txt
    python chromeline.py
