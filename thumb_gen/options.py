import  os
import  sys
import  getopt

from .viewer        import args_error, helps, deco
from .version       import __version__
from .viewer        import configurations
from .config        import modify_config
from .utils         import CheckIfFileExists

videos = []

def parseOpts(argument_list):
    deco()

    try:
        opts, args = getopt.getopt(argument_list,"cvhf:d:",["config","version","help","file=","dir="])

    except getopt.GetoptError:
        args_error(argument_list)
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helps()
            sys.exit()

        elif opt in("-f", "--file"):
            if arg == '':
                args_error()
                sys.exit()

            else:
                return arg, opt

        elif opt in ("-d", "--dir"):
            return arg, opt

        elif opt in ("-v", "--version"):
            print(__version__)
            sys.exit()

        elif opt in ("-c", "--config"):
            conf_images, conf_image_quality, conf_font, conf_font_size, conf_custom_text, conf_bg_colour, conf_font_colour = configurations()
            if conf_images != 0:
                modify_config('images', conf_images)

            if conf_image_quality != 0:
                modify_config('image_quality', conf_image_quality)

            if conf_font != '0':
                modify_config('font', conf_font)

            if conf_font_size != 0:
                modify_config('font_size', conf_font_size)

            if conf_custom_text != '':
                modify_config('custom_text', conf_custom_text)

            if conf_bg_colour != '':
                modify_config('bg_colour', conf_bg_colour)

            if conf_font_colour != '':
                modify_config('font_colour', conf_font_colour)

            sys.exit()

def begin(args='', opt=''):
    current_folder = os.getcwd()

    if opt in ('-d', '--dir') and args != '':
        if CheckIfFileExists(args):
            for video in os.listdir(args):
                if video.endswith('.mp4') or video.endswith('.mkv'):
                    videos.append(os.path.join(args, video))

        elif CheckIfFileExists(os.path.join(current_folder, args)):
            for video in os.listdir(os.path.join(current_folder, args)):
                if video.endswith('.mp4') or video.endswith('.mkv'):
                    videos.append(os.path.join(current_folder, args, video))

        else:
            print("Folder not found!")
            sys.exit()

    elif opt in ('-f', '--file') and args != '':
        if CheckIfFileExists(args):
            videos.append(args)

        elif CheckIfFileExists(os.path.join(current_folder, args)):
            videos.append(os.path.join(current_folder, args))

        else:
            print("File not found!")
            sys.exit()

    return videos
