import pytest

from thumb_gen   import Generator

#video_path, output_path='', custom_text=True, font_dir='', font_size=0, bg_colour='', font_colour=''

video_path = "/home/sample-mp4-file.mp4"
output_path = "/home/runner/work/thumb-gen/thumb-gen/"

def test_worker_1():
    # Checking whether it gives an error when the required arguments are not given
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10)
        assert False
    except ValueError:
        assert True

def test_worker_2():
    # Checking whether it gives an error when the required arguments are not given
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10)
        assert False
    except ValueError:
        assert True

def test_worker_3():
    # Checking if an error is returned when the required arguments are given
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, columns=10)
        assert True
    except:
        assert False

def test_worker_4():
    # Checking if an error is returned when the required arguments are given
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, imgCount=30)
        assert True
    except:
        assert False

def test_worker_5():
    # Checking if an error is returned when the required arguments are given
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10, imgCount=30)
        assert True
    except:
        assert False

def test_worker_6():
    # check if an get error is returened when image count is lower than rows
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, imgCount=5)
        assert False
    except ValueError:
        assert True

def test_worker_7():
    # check if an get error is returened when image count is lower than columns
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10, imgCount=5)
        assert False
    except ValueError:
        assert True

def test_worker_8():
    # check if an get error is returened when defining 'rows', 'columns' and 'imgCount' at once
    try:
        app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10, rows=5, imgCount=50)
        assert False
    except TypeError:
        assert True

def test_worker_9():
    app = Generator(video_path, output_path=output_path, custom_text="thumb gen")
    test_worker_value = app.run()
    assert test_worker_value == True

def test_worker_10():
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black")
    test_worker_value = app.run()
    assert test_worker_value == True

def test_worker_11():
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=5, rows=10)
    test_worker_value = app.run()
    assert test_worker_value == True
