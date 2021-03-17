from .application   import screenshots, resize, thumb

class Generator:
    def __init__(self, video_path, secure_temp, screenshot_folder, resize_folder):
        self.video_path = video_path
        self.secure_temp = secure_temp
        self.screenshot_folder = screenshot_folder
        self.resize_folder = resize_folder
        print("Processing - {}".format(self.video_path))

    def run(self):
        screenshots(self.video_path, self.screenshot_folder)
        resize(self.screenshot_folder, self.resize_folder)
        thumb(self.video_path, self.resize_folder, self.secure_temp)
