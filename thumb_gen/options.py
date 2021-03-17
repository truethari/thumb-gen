import  os
import  sys
import  getopt

from .viewer         import args_error, helps, deco
from .version       import __version__

videos = []

def parseOpts(argument_list):
    deco()
    input_dir = ''
    input_file = ''
    try:
        opts, args = getopt.getopt(argument_list,"vhf:d:w:",["version","help","where=","file=","dir="])
    except getopt.GetoptError:
        args_error(argument_list)
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helps()
            sys.exit()

        elif opt == "-f" or opt == "--file" or opt == "-w" or opt == "--where":
            if arg == '':
                args_error()
                sys.exit()
            else:
                input_file = arg
                return input_dir, input_file, opt
                break

        elif opt == "-d" or opt == "--dir":
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
