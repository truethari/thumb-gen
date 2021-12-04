import pytest

from thumb_gen   import Generator

#video_path, output_path='', custom_text=True, font_dir='', font_size=0, bg_colour='', font_colour=''

def test_worker_1():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    app = Generator(video_path, output_path, "thumb gen")
    test_worker_value = app.run()
    assert test_worker_value == True

def test_worker_2():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black")
    test_worker_value = app.run()
    assert test_worker_value == True

def test_worker_3():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    try:
        app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10)
        assert False
    except:
        assert True

def test_worker_4():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    try:
        app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10)
        assert False
    except:
        assert True

def test_worker_5():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    try:
        app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, columns=10)
        assert True
    except:
        assert False

def test_worker_6():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    try:
        app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, imgCount=20)
        assert True
    except:
        assert False

def test_worker_6():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen/thumb-gen/"
    try:
        app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, imgCount=5)
        assert False
    except:
        assert True
