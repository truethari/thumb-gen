import os

from ffmpy      import FFmpeg
from videoprops import get_video_properties
from PIL        import Image
from PIL        import ImageFont
from PIL        import ImageDraw

from .config    import read_config
from .utils     import listToString, video_info, get_file_size, convert_unit

def font_info(text, font, font_size):
    font = ImageFont.truetype(font, font_size)
    text_width = font.getsize(text)[0]
    text_height = font.getsize(text)[1]

    return text_width, text_height

def lining(text, font, font_size, image_width):
    lines = {'line1': []}
    tmp_list = []
    return_list = []
    text_list = text.split(" ")
    tmp_list = text_list
    rounds = 0
    loop = True

    while loop:
        list_len = len(text_list)
        paragraph = listToString(tmp_list)
        text_width = font_info(paragraph, font, font_size)[0]

        rounds = rounds + 1

        if not text_width > image_width:
            loop2 = True
            list_number = 0

            while loop2:
                list_number = list_number + 1

                try:
                    tmp_line = lines['line{}'.format(list_number)]
                except KeyError:
                    tmp_line = []

                if '0tKJz' not in tmp_line:
                    lines['line{}'.format(list_number)] = [paragraph]
                    lines['line{}'.format(list_number)].append('0tKJz')

                    for i in range(0, (list_len - rounds) + 1):
                        try:
                            text_list.pop(0)
                        except IndexError:
                            pass

                    tmp_list = text_list
                    rounds = 0
                    loop2 = False

        else:
            tmp_list = tmp_list[:-1]

        if text_list == []:
            loop = False

    r_line = 0

    for line in lines:
        r_line = r_line + 1

        if "0tKJz" in lines['line{}'.format(r_line)]:
            lines['line{}'.format(r_line)].remove("0tKJz")

    return lines

def imageText(video_path, secure_tmp, bg_width, bg_height):
    font_name = read_config('font')
    font_size = read_config('font_size')
    custom_text = read_config('custom_text')

    filename = video_path.split("/")
    filename = filename[-1]

    #file
    info_filename = "Filename: " + filename
    info_filesize = "Size: " + str(get_file_size(video_path)) + "MB"
    info_duration = "Duration: " + video_info(video_path)[0]['duration']
    avg_bitrate = convert_unit((float(video_info(video_path)[0]['bit_rate']) + float(video_info(video_path)[1]['bit_rate'])) // 2, unit = "SIZE_UNIT.KB")
    info_avgbitrate = "avg. Bitrate: " + str(avg_bitrate) + "KB/s"
    #video
    info_video = "Video: " + video_info(video_path)[0]['codec_name']
    info_video_res = str(video_info(video_path)[0]['width']) + 'x' + str(video_info(video_path)[0]['height'])
    info_video_bitrate = 'bitrate = ' + str(convert_unit(float(video_info(video_path)[0]['bit_rate']), unit = "SIZE_UNIT.KB")) + "KB/s"
    video_fps = video_info(video_path)[0]['avg_frame_rate'].split('/')
    video_fps = round(int(video_fps[0]) / int(video_fps[1]), 2)
    info_video_fps = str(video_fps) + 'fps'
    #audio
    info_audio = "Audio: " + video_info(video_path)[1]['codec_name']
    info_audio_rate = str(video_info(video_path)[1]['sample_rate']) + 'Hz'
    info_audio_channels = str(video_info(video_path)[1]['channels']) + ' channels'
    info_audio_bitrate = 'bitrate = ' + str(convert_unit(float(video_info(video_path)[1]['bit_rate']), unit = "SIZE_UNIT.KB")) + "KB/s"
    #custom
    custom_text_bx = custom_text

    info_line2 = info_filesize + '    '  + info_duration + '    '  + info_avgbitrate
    info_line3 = info_video + '    '  + info_video_res + '    '  + info_video_bitrate + '    '  + info_video_fps
    info_line4 = info_audio + '    '  + info_audio_rate + '    '  + info_audio_channels + '    ' + info_audio_bitrate

    font_height_filename = 0
    font_height_normal = font_info(info_duration, font_name, font_size)[1]
    font_height_custom_text = 0

    filename_text_lines = lining(custom_text_bx, font_name, font_size, bg_width)
    rounds = 0
    for items in filename_text_lines:
        rounds = rounds + 1
        for lines in filename_text_lines['line{}'.format(rounds)]:
            if lines != []:
                font_height = font_info(lines, font_name, font_size)[1]
                font_height_filename = font_height_filename + font_height + 5

    custom_text_lines = lining(custom_text_bx, font_name, font_size, bg_width)
    rounds = 0
    for items in custom_text_lines:
        rounds = rounds + 1
        for lines in custom_text_lines['line{}'.format(rounds)]:
            if lines != []:
                font_height = font_info(lines, font_name, font_size)[1]
                font_height_custom_text = font_height_custom_text + font_height + 5

    text_area_height = font_height_filename + font_height_normal * 3 + font_height_custom_text + 25

    bg_new_height = text_area_height + bg_height

    img = Image.new('RGB', (bg_width, bg_new_height), color = 'white')
    img.save(secure_tmp + 'bg.png')

    background = Image.open(secure_tmp + 'bg.png')
    org_width, org_height = background.size

    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype(font_name, font_size)

    x = 10
    y = 10

    rounds = 0

    #line1
    info_filename_line = lining(info_filename, font_name, font_size, bg_width)
    for items in info_filename_line:
        rounds = rounds + 1
        for lines in info_filename_line['line{}'.format(rounds)]:
            if lines != []:
                font_width, font_height = font_info(info_filename, font_name, font_size)
                draw.text((x, y), lines, 'black', font=font)
                y = y + font_height

    font_width, font_height = font_info(info_filesize, font_name, font_size)

    #line2
    draw.text((x, y), info_line2, 'black', font=font)
    y = y + 5 + font_height

    #line3
    draw.text((x, y), info_line3, 'black', font=font)
    y = y + 5 + font_height

    #line4
    draw.text((x, y), info_line4, 'black', font=font)
    y = y + 5 + font_height

    rounds = 0
    if not custom_text == '':
        text_lines = lining(custom_text, font_name, font_size, org_width)
        for items in text_lines:
            rounds = rounds + 1
            for lines in text_lines['line{}'.format(rounds)]:
                if lines != []:
                    font_width, font_height = font_info(lines, font_name, font_size)
                    draw.text((x, y), lines, 'black', font=font)
                    y = y + 5 + font_height

    background.save(secure_tmp + 'bg.png')
    return y + 10

def screenshots(video_path, screenshot_folder):
    for img in os.listdir(screenshot_folder):
        os.remove(screenshot_folder + img)

    tm_video_path = video_path.split("/")

    video_properties = get_video_properties(video_path)
    video_duration = int(round(float(video_properties['duration']), 2))
    frame_time = round((video_duration / read_config('images')), 2)

    screenshot_path = screenshot_folder + tm_video_path[-1]
    event = FFmpeg(inputs={video_path: None}, \
            outputs={screenshot_path + '_screen%d.png': \
            ['-hide_banner', '-nostats', '-loglevel', '0', '-vf', 'fps=1/' + str(frame_time)]})
    event.run()

    return True

def resize(screenshot_folder, resize_folder):
    for img in os.listdir(resize_folder):
        os.remove(resize_folder + img)

    for img in os.listdir(screenshot_folder):
        image = Image.open(screenshot_folder + img)
        org_width, org_height = image.size

        new_height = 300 * org_height / org_width

        resized_im = image.resize((300, round(new_height)))
        resized_im.save(resize_folder + 'resized_' + img)

    return True

def thumb(video_path, output_folder, resize_folder, secure_temp):
    for img in os.listdir(resize_folder):
        image = Image.open(resize_folder + img)
        r_new_width, new_height = image.size
        break

    img_rows = read_config('images') / 3
    tmp_var = str(img_rows).split('.')
    if tmp_var[1] != '0':
        img_rows = int(img_rows) + 1

    bg_new_width = int((r_new_width * 3) + 20)
    bg_new_height = int((new_height * img_rows) + (14 * (img_rows)))

    y = imageText(video_path, secure_temp, bg_new_width, bg_new_height)

    backgroud = Image.open(secure_temp + 'bg.png')

    img_list = []
    for img in os.listdir(resize_folder):
        image = Image.open(resize_folder + img)
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

    back_im.save(output_folder[:-4] + '.png', quality=read_config('image_quality'))
    print('The thumbnail was saved in - {}\n'.format(output_folder[:-4] + '.png'))

    return True
