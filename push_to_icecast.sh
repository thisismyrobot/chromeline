#!/bin/sh
#
# Steam line in to an Icecast server on localhost:8000.
#
# Call with PulseAudio device name and Icecast password.
#
# e.g:
#
#     ./push_to_icecast.sh alsa_input.usb-046d_0825_EC767E00-02-U0x46d0x825.analog-mono hackme
#
# Assumes a bog-standard Icecast 2 install and mounts as /chromeline.ogg in
# Icecast so you can listen via:
#
#     http://[this ip]:8000/chromeline.ogg
#

gst-launch-1.0 \
    pulsesrc device=$1 ! \
    audioconvert ! \
    vorbisenc quality=1 ! \
    oggmux max-delay=0 max-page-delay=0 ! \
    shout2send mount=/chromeline.ogg port=8000 ip=127.0.0.1 password=$2
