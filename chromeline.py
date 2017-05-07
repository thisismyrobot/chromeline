"""Cast a Pi line in to a Chromecast."""
import ConfigParser
import os
import signal
import subprocess
import time

import pychromecast


def get_chromecast(uuid):
    """Return the target Chromecast, or None."""
    try:
        return [chromecast
                for chromecast
                in pychromecast.get_chromecasts()
                if str(chromecast.device.uuid) == uuid][0]
    except IndexError:
        pass


def enable_stream(audio_device, password):
    """Start the stream, restart it on error."""
    cmd = ['./push_to_icecast.sh', audio_device, password]
    return subprocess.Popen(cmd, preexec_fn=os.setsid)


def cast_stream(chromecast, stream_source_ip, mount='chromeline.ogg'):
    """Tell the Chromecast about the stream."""
    url = 'http://{}:8000/{}'.format(stream_source_ip, mount)
    chromecast.media_controller.play_media(url, 'audio/ogg')


def load_config():
    """Load the configuration file."""
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    return dict(config.items('chromeline'))


def enable_pulseaudio():
    """This is dumb, but needs to be done."""
    subprocess.call(['pulseaudio', '-D'])


def chromecast_still_connected(chromecast):
    """Seems to be the bulletproof way to work this out."""
    return not chromecast.socket_client.heartbeat_controller.is_expired()


def chromeline(chromecast_uuid, stream_source_ip, line_in_device, icecast_password):
    """Connect it all up."""
    chromecast = None
    while chromecast is None:
        print 'Searching for Chromecast...'
        time.sleep(5)
        chromecast = get_chromecast(chromecast_uuid)

    print 'Mounting internal stream in Icecast...'
    process = enable_stream(line_in_device, icecast_password)
    time.sleep(5)

    print 'Casting external stream to Chromecast...'
    cast_stream(chromecast, stream_source_ip)

    print 'Running...'
    return chromecast, process


def main():
    """Main loop."""
    enable_pulseaudio()

    while True:

        conf = load_config()
        chromecast, process = chromeline(**conf)

        while True:
            time.sleep(5)

            if not chromecast_still_connected(chromecast):
                print 'Stopping internal stream due to Chromecast disconnect!'
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                process.kill()
                break

            if process.poll() is not None:
                print 'Restarting due to internal stream failing!'
                break

        time.sleep(5)


if __name__ == '__main__':
    main()
