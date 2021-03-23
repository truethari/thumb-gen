import os
import tempfile

from .application   import screenshots, resize, thumb

class Generator:
    def __init__(self, video_path, output_path=''):
        self.video_path = video_path

        if output_path == '':
            self.output_path = self.video_path
        else:
            self.output_path = output_path

        self.temp_dir = tempfile.TemporaryDirectory()
        self.secure_temp = self.temp_dir.name + '/'
        self.secure_temp = self.secure_temp.replace("\\", "/")
        self.screenshot_folder = self.secure_temp + '/screenshots/'
        self.resize_folder = self.secure_temp + '/resized/'
        os.mkdir(self.screenshot_folder)
        os.mkdir(self.resize_folder)
        print("Processing - {}".format(self.video_path))

    def run(self):
        screenshots(self.video_path, self.screenshot_folder)
        resize(self.screenshot_folder, self.resize_folder)
        thumb(self.video_path, self.output_path, self.resize_folder, self.secure_temp)
