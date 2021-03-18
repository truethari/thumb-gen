import os
import sys
import pathlib
import configparser

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

def create_config(IMAGES=12, IMAGE_QUALITY=80):
    my_datadir = get_datadir() / "thumb-gen"

    try:
        my_datadir.mkdir(parents=True)

    except FileExistsError:
        pass

    finally:
        configfile_path = str(my_datadir) + "/config.ini"
        config_object = configparser.ConfigParser()
        config_object["DEFAULT"] = {"images": IMAGES, "image_quality": IMAGE_QUALITY}
        with open(configfile_path, 'w') as conf:
            config_object.write(conf)

        return True

def modify_config(options, value_1, value_2=0):
    my_datadir = get_datadir() / "thumb-gen"
    configfile_path = str(my_datadir) + "/config.ini"
    config_object  = configparser.ConfigParser()

    config_object.read(configfile_path)
    userinfo = config_object["DEFAULT"]

    if options == "images_image_quality":
        userinfo["images"] = str(value_1)
        userinfo["image_quality"] = str(value_2)
    elif options == "images":
        userinfo["images"] = str(value_1)
    elif options == "image_quality":
        userinfo["image_quality"] = str(value_1)

    with open(configfile_path, 'w') as conf:
        config_object.write(conf)
    
    return True

def read_config(option):
    my_datadir = get_datadir() / "thumb-gen"
    configfile_path = str(my_datadir) + "/config.ini"
    config_object = configparser.ConfigParser()

    if os.path.isfile(configfile_path):
        config_object.read(configfile_path)
        default = config_object["DEFAULT"]
    else:
        create_config_return = create_config()
        if create_config_return:
            config_object.read(configfile_path)
            default = config_object["DEFAULT"]

    if option == 'images':
        return int(default['images'])
    elif option == 'image_quality':
        return int(default['image_quality'])
