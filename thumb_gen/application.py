import os
import re
import ntpath
import sys
import datetime

from ffmpy      import FFmpeg
from PIL        import Image
from PIL        import ImageFont
from PIL        import ImageDraw
from PIL        import ImageColor

from .config    import read_config
from .utils     import listToString, video_info, get_file_size, convert_unit, packagePath

def font_info(text, font, font_size):
    try:
        font = ImageFont.truetype(font, font_size)
    except OSError:
        font = ImageFont.load_default()

    text_width = font.getsize(text)[0]
    text_height = font.getsize(text)[1]

    return text_width, text_height

def lining(text, font, font_size, image_width):
    lines = {'line1': []}
    tmp_list = []
    text_list = text.split(" ")
    tmp_list = text_list
    rounds = 0

    while True:
        list_len = len(text_list)
        paragraph = listToString(tmp_list)
        text_width = font_info(paragraph, font, font_size)[0]

        rounds = rounds + 1

        if not text_width > image_width:
            list_number = 0

            while True:
                list_number = list_number + 1

                try:
                    tmp_line = lines['line{}'.format(list_number)]
                except KeyError:
                    tmp_line = []

                if '0tKJz' not in tmp_line:
                    lines['line{}'.format(list_number)] = [paragraph]
                    lines['line{}'.format(list_number)].append('0tKJz')

                    for _ in range(0, (list_len - rounds) + 1):
                        try:
                            text_list.pop(0)
                        except IndexError:
                            pass

                    tmp_list = text_list
                    rounds = 0
                    break

        else:
            tmp_list = tmp_list[:-1]

        if text_list == []:
            break

    r_line = 0

    for _ in lines:
        r_line = r_line + 1

        if "0tKJz" in lines['line{}'.format(r_line)]:
            lines['line{}'.format(r_line)].remove("0tKJz")

    return lines

def imageText(video_path, secure_tmp, bg_width, bg_height, custom_text,
              font_dir, font_size, bg_colour, font_colour):
    if font_dir == '':
        font_name = read_config('font')
        if font_name == '':
            package_dir = packagePath()
            font_name = os.path.join(package_dir, 'fonts', 'RobotoCondensed-Regular.ttf')

    else:
        font_name = font_dir

    if font_size == 0:
        font_size = read_config('font_size')

    if custom_text == 'True':
        custom_text = read_config('custom_text')
    elif custom_text == 'False':
        custom_text = ''

    if bg_colour == '':
        bg_colour = read_config('bg_colour')

    if font_colour == '':
        font_colour = read_config('font_colour')

    video_properties, audio_properties, default_properties = video_info(video_path)

    #file
    info_filename = "Filename: " + ntpath.basename(video_path)
    info_filesize = "Size: " + str(get_file_size(video_path)) + "MB"

    try:
        duration = round(float(default_properties['duration']))
        info_duration = "Duration: " + str(datetime.timedelta(seconds=duration))
    except KeyError:
        info_duration = ''
    try:
        avg_bitrate = convert_unit(int(default_properties['bit_rate']))
        info_avgbitrate = "avg. Bitrate: " + str(avg_bitrate) + "KB/s"
    except KeyError:
        info_avgbitrate = ''
    #video
    try:
        info_video = "Video: " + video_properties['codec_name']
    except KeyError:
        info_video = ''
    try:
        info_video_res = str(video_properties['width']) + 'x' + str(video_properties['height'])
    except KeyError:
        info_video_res = ''
    try:
        video_bitrate = video_properties['bit_rate']
        if str(video_bitrate) == 'N/A':
            raise KeyError
        info_video_bitrate = 'bitrate = ' + str(convert_unit(int(video_bitrate))) + "KB/s"
    except KeyError:
        info_video_bitrate = ''
    try:
        video_fps = video_properties['avg_frame_rate'].split('/')
        video_fps = round(int(video_fps[0]) / int(video_fps[1]), 2)
        info_video_fps = str(video_fps) + 'fps'
    except KeyError:
        info_video_fps = ''
    #audio
    try:
        info_audio = "Audio: " + audio_properties['codec_name']
    except KeyError:
        info_audio = ''
    try:
        info_audio_rate = str(audio_properties['sample_rate']) + 'Hz'
    except KeyError:
        info_audio_rate = ''
    try:
        info_audio_channels = str(audio_properties['channels']) + ' channels'
    except KeyError:
        info_audio_channels = ''
    try:
        audio_bitrate = audio_properties['bit_rate']
        if str(audio_bitrate) == 'N/A':
            raise KeyError
        info_audio_bitrate = 'bitrate = ' + str(convert_unit(int(audio_bitrate))) + "KB/s"
    except KeyError:
        info_audio_bitrate = ''
    #custom
    custom_text_bx = custom_text

    info_line2 = info_filesize + '    ' + info_duration + '    ' + info_avgbitrate
    info_line3 = info_video + '    ' + info_video_res + '    ' \
                 + info_video_bitrate + '    ' + info_video_fps
    info_line4 = info_audio + '    ' + info_audio_rate + '    ' \
                 + info_audio_channels + '    ' + info_audio_bitrate

    font_height_filename = 0
    font_height_normal = font_info(info_duration, font_name, font_size)[1]
    font_height_custom_text = 0

    filename_text_lines = lining(info_filename, font_name, font_size, bg_width)
    rounds = 0
    for _ in filename_text_lines:
        rounds = rounds + 1
        for lines in filename_text_lines['line{}'.format(rounds)]:
            if lines != []:
                font_height = font_info(lines, font_name, font_size)[1]
                font_height_filename = font_height_filename + font_height + 5

    rounds = 0
    if custom_text_bx != '':
        custom_text_lines = lining(custom_text_bx, font_name, font_size, bg_width)
        for _ in custom_text_lines:
            rounds = rounds + 1
            for lines in custom_text_lines['line{}'.format(rounds)]:
                if lines != []:
                    font_height = font_info(lines, font_name, font_size)[1]
                    font_height_custom_text = font_height_custom_text + font_height

    valid_lines = 0
    for i in (info_line2, info_line3, info_line4):
        if len(i) - i.count(" ") != 0:
            valid_lines += 1

    text_area_height = 5 + font_height_filename + (font_height_normal + 5) * valid_lines \
                       + font_height_custom_text

    bg_new_height = text_area_height + bg_height

    try:
        bg_colour = ImageColor.getrgb(bg_colour)
    except ValueError:
        bg_colour = bg_colour
        print("ValueError: unknown color specifier: {}".format(bg_colour))
        print("This can be fixed by changing the configurations.\n" \
              "Ex: Background colour = 'white'  /  Background colour = '#ffffff'")
        sys.exit()

    try:
        font_colour = ImageColor.getrgb(font_colour)
    except ValueError:
        font_colour = font_colour
        print("ValueError: unknown color specifier: {}".format(font_colour))
        print("This can be fixed by changing the configurations.\n" \
              "Ex: Font colour = 'black'  / Font colour = '#ffffff'")
        sys.exit()

    img = Image.new('RGB', (bg_width, bg_new_height), bg_colour)
    img.save(os.path.join(secure_tmp, 'bg.png'))

    background = Image.open(os.path.join(secure_tmp, 'bg.png'))
    org_width = background.size[0]

    draw = ImageDraw.Draw(background)

    try:
        font = ImageFont.truetype(font_name, font_size)
    except OSError:
        print("{} file not found! Default font is loaded.".format(font_name))
        package_dir = packagePath()
        font_name = os.path.join(package_dir, 'fonts', 'RobotoCondensed-Regular.ttf')
        font = ImageFont.truetype(font_name, font_size)

    x = 10
    y = 5

    rounds = 0

    #line1
    info_filename_line = lining(info_filename, font_name, font_size, bg_width)
    for _ in info_filename_line:
        rounds = rounds + 1
        for lines in info_filename_line['line{}'.format(rounds)]:
            if lines != []:
                font_height = font_info(info_filename, font_name, font_size)[1]
                draw.text((x, y), lines, font_colour, font=font)
                y = y + font_height

    font_height = font_info(info_filesize, font_name, font_size)[1]

    #line2
    if len(info_line2) - info_line2.count(" ") != 0:
        draw.text((x, y), info_line2, font_colour, font=font)
        y = y + 5 + font_height

    #line3
    if len(info_line3) - info_line3.count(" ") != 0:
        draw.text((x, y), info_line3, font_colour, font=font)
        y = y + 5 + font_height

    #line4
    if len(info_line4) - info_line4.count(" ") != 0:
        draw.text((x, y), info_line4, font_colour, font=font)
        y = y + 5 + font_height

    rounds = 0
    if custom_text != '':
        text_lines = lining(custom_text, font_name, font_size, org_width)
        for _ in text_lines:
            rounds = rounds + 1
            for lines in text_lines['line{}'.format(rounds)]:
                if lines != []:
                    font_height = font_info(lines, font_name, font_size)[1]
                    draw.text((x, y), lines, font_colour, font=font)
                    y = y + font_height
    y = y + 5

    background.save(os.path.join(secure_tmp, 'bg.png'))

    return y + 5

def screenshots(video_path, screenshot_folder):
    for img in os.listdir(screenshot_folder):
        os.remove(os.path.join(screenshot_folder, img))

    video_duration = int(round(float(video_info(video_path)[2]['duration']), 2))
    frame_time = round(video_duration / read_config('images'), 2)

    event = FFmpeg(inputs={video_path: None}, \
            outputs={os.path.join(screenshot_folder, '%d.png'): \
            ['-hide_banner', '-nostats', '-loglevel', '0', '-vf', 'fps=1/' + str(frame_time)]})
    event.run()

    return True

def resize(screenshot_folder, resize_folder):
    for img in os.listdir(resize_folder):
        os.remove(resize_folder + img)

    for img in os.listdir(screenshot_folder):
        image = Image.open(os.path.join(screenshot_folder, img))
        org_width, org_height = image.size

        new_height = 300 * org_height / org_width

        resized_im = image.resize((300, round(new_height)))
        resized_im.save(os.path.join(resize_folder, img))

    return True

def thumb(video_path, output_folder, resize_folder, secure_temp, custom_text,
          font_dir, font_size, bg_colour, font_colour):
    for img in os.listdir(resize_folder):
        image = Image.open(os.path.join(resize_folder, img))
        r_new_width, new_height = image.size
        break

    img_rows = read_config('images') / 3
    tmp_var = str(img_rows).split('.')
    if tmp_var[1] != '0':
        img_rows = int(img_rows) + 1
    img_rows = int(img_rows)

    bg_new_width = int((r_new_width * 3) + 20)
    bg_new_height = int((new_height * img_rows) + ((5 * img_rows) + 5))

    y = imageText(video_path, secure_temp, bg_new_width, bg_new_height, custom_text,
                  font_dir, font_size, bg_colour, font_colour)

    backgroud = Image.open(os.path.join(secure_temp, 'bg.png'))

    img_list = []
    resized_images = os.listdir(resize_folder)
    resized_images.sort(key=lambda f: int(re.sub('\\D', '', f)))

    for img in resized_images:
        image = Image.open(os.path.join(resize_folder, img))
        img_list.append(image)

    back_im = backgroud.copy()

    count = 0
    x = 5
    for img in img_list:
        count =  count + 1
        if (count - 1) % 3 == 0 and count != 1:
            y = y + new_height + 5
            x = 5

        back_im.paste(img_list[count - 1], (x, y))
        x = x + r_new_width + 5

    back_im.save(output_folder + '.png', quality=read_config('image_quality'))

    return True
