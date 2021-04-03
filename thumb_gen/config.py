import os
import configparser

from .utils     import get_datadir, CheckIfFileExists
from .version   import config_version

def create_config(IMAGES=12, IMAGE_QUALITY=80, FONT='', FONT_SIZE=30, CUSTOM_TEXT='', BG_COLOUR='white', FONT_COLOUR='black'):
    my_datadir = get_datadir() / "thumb-gen"

    try:
        my_datadir.mkdir(parents=True)

    except FileExistsError:
        pass

    finally:
        configfile_path = os.path.join(str(my_datadir), "config.ini")
        config_object = configparser.ConfigParser()
        config_object["DEFAULT"] = {"images": IMAGES, "image_quality": IMAGE_QUALITY, "font":FONT, "font_size":FONT_SIZE, "custom_text":CUSTOM_TEXT, "bg_colour":BG_COLOUR, "font_colour":FONT_COLOUR}
        config_object["VERSION"] = {"config_version": config_version}
        with open(configfile_path, 'w') as conf:
            config_object.write(conf)

        return True

def modify_config(options, value):
    my_datadir = get_datadir() / "thumb-gen"
    configfile_path = os.path.join(str(my_datadir), "config.ini")
    config_object  = configparser.ConfigParser()

    config_object.read(configfile_path)
    userinfo = config_object["DEFAULT"]

    if options == "images":
        userinfo["images"] = str(value)

    elif options == "image_quality":
        userinfo["image_quality"] = str(value)

    elif options == "font":
        userinfo["font"] = str(value)

    elif options == "font_size":
        userinfo["font_size"] = str(value)

    elif options == "custom_text":
        if value == '000' or value == 'clear':
            userinfo["custom_text"] = ''
        else:
            userinfo["custom_text"] = str(value)

    elif options == "bg_colour":
        userinfo["bg_colour"] = str(value)

    elif options == "font_colour":
        userinfo["font_colour"] = str(value)

    with open(configfile_path, 'w') as conf:
        config_object.write(conf)

    return True

def read_config(option):
    my_datadir = get_datadir() / "thumb-gen"
    configfile_path = os.path.join(str(my_datadir), "config.ini")
    config_object = configparser.ConfigParser()

    if CheckIfFileExists(configfile_path):
        config_object.read(configfile_path)

        try:
            config_object["VERSION"]["config_version"] == config_version
        except KeyError:
            create_config()

        config_object.read(configfile_path)
        if config_object["VERSION"]["config_version"] == config_version:
            default = config_object["DEFAULT"]

        else:
            create_config_return = create_config()
            if create_config_return:
                config_object.read(configfile_path)
                default = config_object["DEFAULT"]

    else:
        create_config_return = create_config()
        if create_config_return:
            config_object.read(configfile_path)
            default = config_object["DEFAULT"]

    loop = True
    while loop:
        try:
            if option == 'images':
                return int(default['images'])
            elif option == 'image_quality':
                return int(default['image_quality'])
            elif option == 'font':
                return str(default['font'])
            elif option == 'font_size':
                return int(default['font_size'])
            elif option == 'custom_text':
                return str(default['custom_text'])
            elif option == 'bg_colour':
                return str(default['bg_colour'])
            elif option == 'font_colour':
                return str(default['font_colour'])
            loop = False

        except KeyError:
            create_config_return = create_config()
            if create_config_return:
                config_object.read(configfile_path)
                default = config_object["DEFAULT"]
