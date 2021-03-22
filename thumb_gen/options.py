import  os
import  sys
import  getopt

from .viewer        import args_error, helps, deco
from .version       import __version__
from .viewer        import configurations
from .config        import modify_config

videos = []

def parseOpts(argument_list):
    deco()
    input_dir = ''
    input_file = ''

    try:
        opts, args = getopt.getopt(argument_list,"cvhf:d:w:",["config","version","help","file=","dir=","where="])
    
    except getopt.GetoptError:
        args_error(argument_list)
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helps()
            sys.exit()

        elif opt in("-f", "--file", "-w", "--where"):
            if arg == '':
                args_error()
                sys.exit()
            else:
                input_file = arg
                return input_dir, input_file, opt
                break

        elif opt in ("-d", "--dir"):
            if arg == '':
                args_error()
                sys.exit()
            else:
                input_dir = arg
                return input_dir, input_file, opt
                break

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

    elif (opt == '-d' or opt == '--dir') and input_dir != '':
        input_dir = input_dir.replace("\\", "/")
        for video in os.listdir(input_dir):
            if video.endswith('.mp4') or video.endswith('.mkv'):
                videos.append(input_dir + '/' + video)

    elif (opt == '-f' or opt == '--file') and input_file != '':
        current_folder = os.getcwd() + '/'
        current_folder = current_folder.replace("\\", "/")
        videos.append(current_folder + input_file)

    elif (opt == '-w' or opt == '-where') and input_file !='':
        input_file = input_file.replace("\\", "/")
        videos.append(input_file)

    return videos
