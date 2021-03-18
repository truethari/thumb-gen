import os

from ffmpy       import FFmpeg
from videoprops  import get_video_properties
from PIL         import Image

from .config     import read_config

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

def thumb(video_path, resize_folder, secure_temp):
    for img in os.listdir(resize_folder):
        image = Image.open(resize_folder + img)
        r_new_width, new_height = image.size
        break

    img_rows = read_config('images') / 3
    tmp_var = str(img_rows).split('.')
    if tmp_var[1] != '0':
        img_rows = int(img_rows) + 1

    bg_new_width = int((r_new_width * 3) + 20)
    bg_new_height = int((new_height * img_rows) + (img_rows * 5) + 5)

    img = Image.new('RGB', (bg_new_width, bg_new_height), color = 'white')
    img.save(secure_temp + 'bg.png')
    backgroud = Image.open(secure_temp + 'bg.png')

    img_list = []
    for img in os.listdir(resize_folder):
        image = Image.open(resize_folder + img)
        img_list.append(image)

    back_im = backgroud.copy()

    count = 0
    x = y = 5
    for img in img_list:
        count =  count + 1
        if (count - 1) % 3 == 0 and count != 1:
            y = y + new_height + 5
            x = 5

        back_im.paste(img_list[count - 1], (x, y))
        x = x + r_new_width + 5

    back_im.save(video_path[:-4] + '.png', quality=read_config('image_quality'))
    print('The thumbnail was saved in - {}\n'.format(video_path[:-4] + '.png'))

    return True
