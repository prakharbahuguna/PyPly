import subprocess

__author__ = 'prakhar'
osabin = 'osascript'
osaflag = '-e'
osacommand = 'tell application "Spotify" to'


def play_track(trackid):
    cmd = '{} play track "{}"'.format(osacommand, trackid)
    subprocess.call([osabin, osaflag, cmd])


def play_pause():
    cmd = '{} playpause'.format(osacommand)
    subprocess.call([osabin, osaflag, cmd])


def skip_track():
    cmd = '{} next track'.format(osacommand)
    subprocess.call([osabin, osaflag, cmd])


def track_id():
    cmd = '{} id of current track'.format(osacommand)
    return subprocess.check_output([osabin, osaflag, cmd])[:-1]


def track_name():
    cmd = '{} name of current track'.format(osacommand)
    return subprocess.check_output([osabin, osaflag, cmd])[:-1]


def track_artist():
    cmd = '{} artist of current track'.format(osacommand)
    return subprocess.check_output([osabin, osaflag, cmd])[:-1]