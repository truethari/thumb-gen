import  os
import pytest
import  tempfile

from    thumb_gen.application  import  screenshots, resize, thumb

temp_dir = tempfile.TemporaryDirectory()
secure_temp = temp_dir.name + '/'
secure_temp = secure_temp.replace("\\", "/")
screenshot_folder = secure_temp + '/screenshots/'
resize_folder = secure_temp + '/resized/'
output_path = '/home/travis/build/truethari/thumb-gen/'
os.mkdir(screenshot_folder)
os.mkdir(resize_folder)

#video_path = '/tests/testdata/input/input.mp4'
video_path = "/home/sample-mp4-file.mp4"

def test_screenshots():
    test_screenshots_value = screenshots(video_path, screenshot_folder)
    assert test_screenshots_value == 1

def test_resize():
    test_resize_value = resize(screenshot_folder, resize_folder)
    assert test_resize_value == 1

def test_thumb():
    test_thumb_value = thumb(output_path, resize_folder, secure_temp)
    assert test_thumb_value == 1
