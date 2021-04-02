import os
import sys
import pathlib

from videoprops  import get_video_properties, get_audio_properties

import thumb_gen as _

def get_datadir() -> pathlib.Path:

    """
    Returns a parent directory path
    where persistent application data can be stored.

    # linux: ~/.local/share
    # macOS: ~/Library/Application Support
    # windows: C:/Users/<USER>/AppData/Roaming
    """

    home = pathlib.Path.home()

    if sys.platform == "win32":
        return home / "AppData/Roaming"
    elif sys.platform == "linux":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"

def check_os():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'linux':
        return 'linux'
    elif sys.platform == 'darwin':
        return 'darwin'

def listToString(s, chars=" "):
    str1 = chars
    if chars == 'sys':
        oss = check_os()
        if oss == 'win32':
            return ('\\'.join(s))
        else:
            return ('/'.join(s))
    else:
        return (str1.join(s))

def video_info(video_path):
    video_properties = get_video_properties(video_path)
    audio_properties = get_audio_properties(video_path)
    return video_properties, audio_properties

def convert_unit(size_in_bytes, unit='KB'):
    if unit == "KB":
        return round((size_in_bytes/1024), 2)
    elif unit == "MB":
        return round(size_in_bytes/(1024*1024), 2)
    elif unit == "GB":
        return round(size_in_bytes/(1024*1024*1024), 2)
    else:
        return size_in_bytes

def get_file_size(file_name, unit="MB"):
    size = os.path.getsize(file_name)
    return convert_unit(size, unit)

def CheckIfFileExists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

def packagePath():
    return _.__path__[0]
