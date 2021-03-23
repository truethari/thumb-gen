import enum
import os

from os import path
from videoprops  import get_video_properties, get_audio_properties

def listToString(s):
    str1 = " "
    return (str1.join(s))

def video_info(video_path):
    video_properties = get_video_properties(video_path)
    audio_properties = get_audio_properties(video_path)
    return video_properties, audio_properties

class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4

def convert_unit(size_in_bytes, unit):
    if unit == "SIZE_UNIT.KB":
        return round((size_in_bytes/1024), 2)
    elif unit == "SIZE_UNIT.MB":
        return round(size_in_bytes/(1024*1024), 2)
    elif unit == "SIZE_UNIT.GB":
        return round(size_in_bytes/(1024*1024*1024), 2)
    else:
        return size_in_bytes

def get_file_size(file_name, size_type = "SIZE_UNIT.MB" ):
   size = os.path.getsize(file_name)
   return convert_unit(size, size_type)

def CheckIfFileExists(file_path):
    if path.exists(file_path):
        return True
    else:
        return False