import sys

from datetime   import datetime
from PIL        import ImageColor
from .config    import read_config
from .utils     import CheckIfFileExists, check_os

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def configurations():
        print("Configurations\n")
        print("Images = {}\n" \
              "Thumbnail Quality = {}\n" \
              "Font = {}\n" \
              "Font Size = {}\n" \
              "Custom Text = {}\n" \
              "Background Colour = {}\n" \
              "Font Colour = {}\n" \
              .format(read_config('images'), \
                      read_config('image_quality'), \
                      read_config('font'), \
                      read_config('font_size'), \
                      read_config('custom_text'), \
                      read_config('bg_colour'), \
                      read_config('font_colour')))

        while True:
                try:
                        while True:
                                print("If you do not want to change the values, leave the input blank and press Enter.\n")
                                print("CTRL + C to exit.")
                                try:
                                        images = int(input("Images: ") or 0)
                                        break
                                except ValueError:
                                        print("Invalid input! Please enter a valid number.")

                        while True:
                                try:
                                        while True:
                                                image_quality = int(input("Thumbnail Quality (10 - 100): ") or 0)
                                                if 101 > image_quality > 9 or image_quality == 0:
                                                        break
                                                else:
                                                        print("Enter number between 10 - 100!")
                                        break
                                except ValueError:
                                        print("Invalid input! Please enter a valid number.")

                        while True:
                                font_path = str(input("Font Path: ") or '0')
                                font_path_status = CheckIfFileExists(font_path)
                                if font_path_status or font_path == '0':
                                        break
                                else:
                                        print("No font file found. Check the path and re-enter it")

                        while True:
                                try:
                                        while True:
                                                font_size = int(input("Font Size (10 - 100): ") or 0)
                                                if 9 < font_size < 101 or font_size == 0:
                                                        break
                                                else:
                                                        print("Enter number between 10 - 100!")
                                        break
                                except ValueError:
                                        print("Invalid input! Please enter a valid number.")

                        print("Input 'clear' or '000' to clear custom text")
                        custom_text = str(input("Custom text: ") or '')

                        while True:
                                try:
                                        bg_colour = str(input("Background Colour: ") or '')
                                        if bg_colour == '':
                                                pass
                                        else:
                                                ImageColor.getrgb(bg_colour)
                                except ValueError:
                                        print("Color not recognized: {}. Enter a valid colour!".format(bg_colour))
                                else:
                                        break

                        while True:
                                try:
                                        font_colour = str(input("Font Colour: ") or '')
                                        if font_colour == '':
                                                pass
                                        else:
                                                ImageColor.getrgb(font_colour)
                                except ValueError:
                                        print("Color not recognized: {}. Enter a valid colour!".format(font_colour))
                                else:
                                        break

                except KeyboardInterrupt:
                        sys.exit('\n')

                break

        return images, image_quality, font_path, font_size, custom_text, bg_colour, font_colour

def print_process(name):
        oss = check_os()
        if oss == 'linux':
                print("\033[33m [{}]  \033[36m Processing: {}\033[00m" .format(current_time, name))
        else:
                print(" [{}]   Processing: {}".format(current_time, name))

def print_success(name):
    oss = check_os()
    if oss == 'linux':
        print("\033[33m [{}]  \033[36m Thumbnail saved in: {}\033[00m" .format(current_time, name))
    else:
        print(" [{}]   Thumbnail saved in: {}".format(current_time, name))
