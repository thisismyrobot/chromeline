#!/bin/sh

sudo apt-get update

sudo apt-get install -y \
    pulseaudio \
    gstreamer1.0-tools \
    icecast2 \
    gstreamer1.0-pulseaudio
