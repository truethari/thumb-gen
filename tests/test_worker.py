import pytest

from thumb_gen.worker   import Generator

def test_worker():
    #video_path, output_path='', custom_text='True', font_dir='', font_size=0
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    custom_text = "thumb gen"
    app = Generator(video_path, output_path, custom_text)
    test_worker_value = app.run()
    assert test_worker_value == True
