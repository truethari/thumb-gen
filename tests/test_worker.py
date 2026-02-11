import os
import pytest

from thumb_gen import Generator

# Use local files so tests pass both locally and on GitHub Actions
video_path = "sample.mp4" 
output_path = os.getcwd()

def test_worker_1():
    # Checking whether it gives an error when 'columns' is given without 'imgCount'
    with pytest.raises(ValueError):
        Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10)

def test_worker_2():
    # Checking whether it gives an error when 'rows' is given without 'imgCount'
    with pytest.raises(ValueError):
        Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10)

def test_worker_3():
    # Checking if NO error is returned when required arguments are given
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, columns=10)
    assert app is not None

def test_worker_4():
    # Checking if NO error is returned when required arguments are given
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, imgCount=30)
    assert app is not None

def test_worker_5():
    # Checking if NO error is returned when required arguments are given
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10, imgCount=30)
    assert app is not None

def test_worker_6():
    # Check if an error is returned when image count is lower than rows
    with pytest.raises(ValueError):
        Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", rows=10, imgCount=5)

def test_worker_7():
    # Check if an error is returned when image count is lower than columns
    with pytest.raises(ValueError):
        Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10, imgCount=5)

def test_worker_8():
    # Check if an error is returned when defining 'rows', 'columns', and 'imgCount' all at once
    with pytest.raises(TypeError):
        Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=10, rows=5, imgCount=50)

def test_worker_9():
    app = Generator(video_path, output_path=output_path, custom_text="thumb gen")
    assert app.run() == True

def test_worker_10():
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black")
    assert app.run() == True

def test_worker_11():
    app = Generator(video_path, output_path=output_path, font_size=10, bg_colour="yellow", font_colour="black", columns=5, rows=10)
    assert app.run() == True