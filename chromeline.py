"""A helper to cast my record player to my chromecast."""
import pychromecast


CHROMECAST_UUID = '34c7f7e0-852e-bbc8-8de6-85d69192f0f8'


def target_chromecast(uuid):
    """Our target chromecast."""
    try:
        return [chromecast
                for chromecast
                in pychromecast.get_chromecasts()
                if str(chromecast.device.uuid) == uuid][0]
    except IndexError:
        raise Exception('Could not find target chromecast')


def vinylcast():
    """The main loop."""
    target = target_chromecast(CHROMECAST_UUID)
    media_controller = target.media_controller

    # Works!!!
    media_controller.play_media('http://192.168.20.15:8000/vinylcast.ogg', 'audio/ogg')

    import pdb; pdb.set_trace()

if __name__ == '__main__':
    vinylcast()
