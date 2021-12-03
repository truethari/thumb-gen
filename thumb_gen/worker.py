import os
import re
import tempfile

from .application   import screenshots, resize, timestamps, thumb
from .viewer        import print_process, print_success
from .utils         import listToString

class Generator:
    def __init__(self, video_path, rows=0, columns=0, imgCount=0, output_path='', custom_text='True', font_dir='', font_size=0, bg_colour='', font_colour=''):
        self.video_path = video_path
        self.rows = rows
        self.columns = columns
        self.imgCount = imgCount

        if self.imgCount != 0:
            if self.rows == 0 and self.columns == 0:
                pass

            elif self.rows == 0:
                self.rows, mod = divmod(self.imgCount, self.columns)
                if mod != 0 and self.imgCount > self.columns:
                    self.rows += 1

            elif self.columns == 0:
                self.columns, mod = divmod(self.imgCount, self.rows)
                if mod != 0 and self.imgCount > self.rows:
                    self.columns += 1

        if output_path == '':
            self.output_path = self.video_path[:-4]
            self.output_folder = listToString(re.split(pattern = r"[/\\]", string = self.video_path)[:-1], "sys")

        else:
            self.filename = re.split(pattern = r"[/\\]", string = self.video_path)[-1]
            self.output_path = os.path.join(output_path, self.filename[:-4])
            self.output_folder = self.output_path

        self.custom_text = str(custom_text)
        self.font_dir = font_dir

        if isinstance(font_size, int):
            self.font_size = font_size
        elif isinstance(font_size, str):
            raise ValueError("Font size must be an integer")

        self.bg_colour = bg_colour
        self.font_colour = font_colour

        self.temp_dir = tempfile.TemporaryDirectory()
        self.secure_temp = self.temp_dir.name
        self.screenshot_folder = os.path.join(self.secure_temp, 'screenshots')
        self.resize_folder = os.path.join(self.secure_temp, 'resized')
        os.mkdir(self.screenshot_folder)
        os.mkdir(self.resize_folder)

    def run(self):
        print_process(self.video_path)
        self.ss_time = screenshots(self.video_path, self.screenshot_folder, self.imgCount)
        resize(self.screenshot_folder, self.resize_folder)
        timestamps(self.resize_folder, self.font_dir, self.font_size, self.ss_time)
        thumb_out = thumb(self.video_path, self.output_path, self.resize_folder, self.secure_temp, self.custom_text, self.font_dir, self.font_size, self.bg_colour, self.font_colour)

        if thumb_out:
            print_success(self.output_folder)

        return True
