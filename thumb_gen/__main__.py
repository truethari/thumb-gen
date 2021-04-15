import os
import sys
import optparse

from .viewer    import configurations
from .config    import modify_config
from .worker    import Generator
from .version   import __version__

def check_files(paths_or_files):
    videos = []
    current_directory = os.getcwd()

    for path_or_file in paths_or_files:
        if not os.path.exists(path_or_file):
            if not os.path.exists(os.path.join(current_directory, path_or_file)):
                sys.exit("{}: no such file or directory".format(path_or_file))
            else:
                real_path = os.path.join(current_directory, path_or_file)
        else:
            if os.path.isfile(path_or_file):
                real_path = path_or_file
            else:
                real_path = os.path.join(current_directory, path_or_file)

        if os.path.isfile(real_path):
            if real_path.endswith('.mp4') or real_path.endswith('.mkv'):
                videos.append(real_path)
            else:
                sys.exit("{}: file not supported".format(real_path))
        elif os.path.isdir(real_path):
            for file in os.listdir(real_path):
                if file.endswith('.mp4') or file.endswith('.mkv'):
                    videos.append(os.path.join(real_path, file))
            if videos == []:
                sys.exit("{}: all of files in the directory are not supported".format(real_path))

    return videos

def main():
    usage = "usage: %prog file file\nusage: %prog dir dir"
    parser = optparse.OptionParser(description="THUMB-GEN v" + __version__, usage=usage)
    parser.add_option("-c", "--config",
            action="store_true",
            default=False,
            help="configurations (images, image quality, font, font size, \
                  custom text, bg color, font color)"
            )
    parser.add_option("-v", "--version",
            action="store_true",
            default=False,
            help="show thumb-gen version and exit"
            )

    (options, args) = parser.parse_args()
    options = vars(options)

    if options['config']:
        conf_images, conf_image_quality, conf_font, conf_font_size, \
        conf_custom_text, conf_bg_colour, conf_font_colour = configurations()

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

    elif options['version']:
        sys.exit(__version__)

    elif args != []:
        videos = check_files(args)
        for video in videos:
            app = Generator(video)
            app.run()

    else:
        print("no argument given!\n")
        parser.print_help()

if __name__ == '__main__':
    main()