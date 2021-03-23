import os
import tempfile

from .application   import screenshots, resize, thumb

class Generator:
    def __init__(self, video_path, output_path='', custom_text='True'):
        self.video_path = video_path

        if output_path == '':
            self.output_path = self.video_path[:-4]
        else:
            self.filename = self.video_path.split("/")
            self.filename = self.filename[-1]
            self.output_path = output_path + "/" + self.filename[:-4]

        self.custom_text = str(custom_text)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.secure_temp = self.temp_dir.name + '/'
        self.secure_temp = self.secure_temp.replace("\\", "/")
        self.screenshot_folder = self.secure_temp + '/screenshots/'
        self.resize_folder = self.secure_temp + '/resized/'
        os.mkdir(self.screenshot_folder)
        os.mkdir(self.resize_folder)

    def run(self):
        print("Processing - {}".format(self.video_path))
        screenshots(self.video_path, self.screenshot_folder)
        resize(self.screenshot_folder, self.resize_folder)
        thumb(self.video_path, self.output_path, self.resize_folder, self.secure_temp, self.custom_text)
