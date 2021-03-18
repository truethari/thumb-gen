import  os
import  sys
import  shutil
import  tempfile

from    .options        import  parseOpts, begin
from    .worker         import  Generator
from    .viewer         import  helps, args_error

temp_dir = tempfile.TemporaryDirectory()
secure_temp = temp_dir.name + '/'
secure_temp = secure_temp.replace("\\", "/")
screenshot_folder = secure_temp + '/screenshots/'
resize_folder = secure_temp + '/resized/'
os.mkdir(screenshot_folder)
os.mkdir(resize_folder)

def run(argument_list = False):
    try:
        input_dir, input_file, opt = parseOpts(argument_list)
    except TypeError:
        args_error()
        sys.exit()
    videos = begin(input_dir, input_file, opt)

    try:
        for video_path in videos:        
            app = Generator(video_path, secure_temp, screenshot_folder, resize_folder)
            app.run()

    finally:
        shutil.rmtree(temp_dir.name)
