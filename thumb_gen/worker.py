import os
import tempfile

from .application   import screenshots, resize, timestamps, thumb
from .viewer        import print_process, print_success

class Generator:
    def __init__(self, video_path, output_path='', rows=0, columns=0, imgCount=0, custom_text='True', font_dir='', font_size=0, bg_colour='', font_colour=''):
        self.video_path = video_path
        self.rows = rows
        self.columns = columns
        self.imgCount = imgCount

        if self.imgCount != 0:
            if self.rows == 0 and self.columns == 0:
                self.columns = 3
                self.rows, mod = divmod(self.imgCount, self.columns)
                if mod != 0 and self.imgCount > self.columns:
                    self.rows += 1

            elif self.rows == 0:
                if self.columns > self.imgCount:
                    raise ValueError("'columns' value greater than 'imgCount'.")
                self.rows, mod = divmod(self.imgCount, self.columns)
                if mod != 0 and self.imgCount > self.columns:
                    self.rows += 1

            elif self.columns == 0:
                if self.rows > self.imgCount:
                    raise ValueError("'rows' value greater than 'imgCount'.")
                self.columns, mod = divmod(self.imgCount, self.rows)
                if mod != 0 and self.imgCount > self.rows:
                    self.columns += 1

            else:
                raise TypeError("defining 'rows', 'columns' and 'imgCount' at once is not functional. remove one of them")
        else:
            if (self.rows == 0 and self.columns != 0) or (self.rows != 0 and self.columns == 0):
                raise ValueError("missing 1 required positional argument: 'imgCount'")

        if 0 < self.imgCount < 3:
            raise ValueError("'imgCount' value must be greater than 3")

        if 0 < self.columns < 3:
            raise ValueError("'columns' value must be greater than 3")

        if output_path == '':
            # better way toany extension length
            self.output_path = os.path.splitext(self.video_path)[0]
            self.output_folder = os.path.dirname(self.video_path)
        else:
            # Extract filename and strip extension
            filename = os.path.basename(self.video_path)
            filename_no_ext = os.path.splitext(filename)[0]
            
            self.output_path = os.path.join(output_path, filename_no_ext)
            self.output_folder = self.output_path

        self.custom_text = str(custom_text)
        self.font_dir = font_dir

        if isinstance(font_size, int):
            self.font_size = font_size
        elif isinstance(font_size, str):
            raise ValueError("'font_size' must be an integer")

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
        thumb_out = thumb(self.video_path,
                          self.rows,
                          self.columns,
                          self.output_path,
                          self.resize_folder,
                          self.secure_temp,
                          self.custom_text,
                          self.font_dir,
                          self.font_size,
                          self.bg_colour,
                          self.font_colour)

        if thumb_out:
            print_success(self.output_folder)

        return True