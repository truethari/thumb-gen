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
    input_dir = ''
    input_file = ''

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
                input_file = arg
                return input_dir, input_file, opt

        elif opt in ("-d", "--dir"):
            if arg == '':
                args_error()
                sys.exit()

            else:
                input_dir = arg
                return input_dir, input_file, opt

        elif opt in ("-v", "--version"):
            print(__version__)
            sys.exit()

        elif opt in ("-c", "--config"):
            conf_images, conf_image_quality, conf_font, conf_font_size, conf_custom_text = configurations()

            if conf_images != 0:
                modify_config('images', conf_images)

            if conf_image_quality != 0:
                modify_config('image_quality', conf_image_quality)

            if conf_font != '0':
                modify_config('font', conf_font)

            if conf_font_size != 0:
                modify_config('font_size', conf_font_size)

            if conf_custom_text != 0:
                modify_config('custom_text', conf_custom_text)

            sys.exit()

def begin(input_dir = '', input_file = '', opt = ''):
    if opt == '-d' and input_dir == '':
        current_folder = os.getcwd() + '/'
        current_folder = current_folder.replace("\\", "/")

        for video in os.listdir(current_folder):
            if video.endswith('.mp4') or video.endswith('.mkv'):
                videos.append(current_folder + video)

    elif opt in ('-d', '--dir') and input_dir != '':
        current_folder = os.getcwd() + '/'
        current_folder = current_folder.replace("\\", "/")

        if CheckIfFileExists(input_dir):
            for video in os.listdir(input_dir):
                if video.endswith('.mp4') or video.endswith('.mkv'):
                    videos.append(input_dir + '/' + video)

        elif CheckIfFileExists(current_folder + input_dir):
            for video in os.listdir(current_folder + input_dir):
                if video.endswith('.mp4') or video.endswith('.mkv'):
                    videos.append(current_folder + input_dir + '/' + video)

        else:
            print("Folder not found!")
            sys.exit()

    elif opt in ('-f', '--file') and input_file != '':
        current_folder = os.getcwd() + '/'
        current_folder = current_folder.replace("\\", "/")

        if CheckIfFileExists(input_file):
            videos.append(input_file)

        elif CheckIfFileExists(current_folder + input_file):
            videos.append(current_folder + input_file)

        else:
            print("File not found!")
            sys.exit()

    return videos
