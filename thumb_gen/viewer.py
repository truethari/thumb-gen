import sys

from .config import read_config

def deco():
        print("""
  _______ _                     _            _____
 |__   __| |                   | |          / ____|           
    | |  | |__  _   _ _ __ ___ | |__ ______| |  __  ___ _ __
    | |  | '_ \| | | | '_ ` _ \| '_ |______| | |_ |/ _ | '_ \ 
    | |  | | | | |_| | | | | | | |_) |     | |__| |  __| | | |
    |_|  |_| |_|\__,_|_| |_| |_|_.__/       \_____|\___|_| |_|

""")

def args_error(argument_list = False):
        if argument_list == False:
                print("Usage: thumb-gen [options] path/file\n\nerror: You must provide at least one option.")
        else:
                print("ERROR: unknown command {}".format(argument_list))

def helps():
        print ("""
    -h, --help          show this help message and exit
    -c, --config        change screenshots for thumbnail image and image quality
    -v, --version       show program's version number and exit

Options:
    -f, --file          input a single video from current directory
    -w, --where         input a single video from another directory
    -d, --dir           input videos from a directory
    """)

def configurations():
        print("Configurations\n")
        print("Images = {}\nThumbnail Quality = {}\n".format(read_config('images'), read_config('image_quality')))

        loop = True
        while loop:
                try:
                        loop2 = True
                        while loop2:
                                print("If you do not want to change the values, leave the input blank and press Enter.\n")
                                print("CTRL + C to exit.")
                                try:
                                        images = int(input("Images = ") or 0)
                                        loop2 = False
                                except ValueError:
                                        print("Invalid input! Please enter a valid number.")
                        loop3 = True
                        while loop3:
                                try:
                                        loop4 = True
                                        while loop4:
                                                image_quality = int(input("Thumbnail Quality (10 - 100) = ") or 0)
                                                if 101 > image_quality > 9 or image_quality == 0:
                                                        loop4 = False
                                                        loop3 = False
                                                else:
                                                        print("Enter number between 10 - 100!")
                                except ValueError:
                                        print("Invalid input! Please enter a valid number.")

                except KeyboardInterrupt:
                        loop = False
                        sys.exit()

                loop = False

        return images, image_quality