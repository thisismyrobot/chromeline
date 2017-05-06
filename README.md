# Live stream line in on a Pi to a Chromecast

## Setup on Pi

Need GStreamer and icecast2 and pulseaudio

    sudo apt-get install pulseaudio gstreamer1.0-tools icecast2 gstreamer1.0-pulseaudio

Then hook up some magic:

    gconftool-2 -t string --set /system/gstreamer/0.10/default/audiosrc pulsesrc

Need to know your input sound card name for the config:

    pactl list

## Icecast configuration

Edit /etc/icecast2/icecast.xml

Change:

    burst-on-connect = 0
    burst-size = 0

Then:

    sudo /etc/init.d/icecast2 restart
