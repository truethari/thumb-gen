# Thumbnail Generator 🎬

[![github actions](https://github.com/truethari/thumb-gen/actions/workflows/thumb-gen.yml/badge.svg)](https://github.com/truethari/thumb-gen/actions/workflows/thumb-gen.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/01b66feeb94743ac80e413e4e9075595)](https://www.codacy.com/gh/truethari/thumb-gen/dashboard?utm_source=github.com&utm_medium=referral&utm_content=truethari/thumb-gen&utm_campaign=Badge_Grade)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://badge.fury.io/py/thumb-gen.svg)](https://badge.fury.io/py/thumb-gen)
[![Downloads](https://pepy.tech/badge/thumb-gen)](https://pepy.tech/project/thumb-gen)

## What is This

---

This is a Python application that can be used to generate video thumbnail for mp4 and mkv file types.

[![Imgur](https://i.imgur.com/qRHQRK7.png)](https://imgur.com/a/xpkkyqH)

## Installation

You can use pip:

```console
~$ pip3 install thumb-gen
```

## Configurations

- The number of screen images that should be included in the final thumbnail image
- Thumbnail image quality
- Font type in the video info panel. You can add a file path of a font file (.ttf) to this
- Font size in the video info panel
- Custom text in the video info panel
- Background color of the thumbnail (Hex codes are also supported)
- Font colour of the thumbnail (Hex codes are also supported)

Download font files : [FontSquirrel](https://www.fontsquirrel.com/)

```console
~$ thumb-gen -c
```

or

```console
~$ thumb-gen --config
```

By program default:

```ini
IMAGES = 12
IMAGE_QUALITY = 80
FONT =
FONT_SIZE = 20
CUSTOM_TEXT =
BG_COLOUR = white
FONT_COLOUR = black
```

## Usage

### Usage options

```text
Usage: thumb-gen file file
usage: thumb-gen dir dir

Options:
  -h, --help     show this help message and exit
  -c, --config   configurations (images, image quality, font, font size,
                 custom text, bg color, font color)
  -v, --version  show thumb-gen version and exit
```

### Console

```console
~$ thumb-gen -h
~$ thumb-gen --help

~$ thumb-gen -c
~$ thumb-gen --config

~$ thumb-gen -v
~$ thumb-gen --version

~$ thumb-gen input.mp4
~$ thumb-gen input.mp4 input2.mp4
~$ thumb-gen "d:/videos/input.mp4"

~$ thumb-gen "/videos"
~$ thumb-gen "/videos" "/videos2"
~$ thumb-gen "d:/videos"
```

### Python

- If you don't set an output folder, thumbnail images will be saved in the video folder (video_path).
- If you don't need a custom text and custom font file (including font size) and you have already set these for the configuration file (using console or defaults), it will be added automatically. To avoid this set the `custom_text` value to `False` and add a custom font file location.
- If you do not set the `columns` size, it will use the default value (3)

```python
Generator(video_path, output_path='', rows=0, columns=0, imgCount=0, custom_text='True', font_dir='', font_size=0, bg_colour='', font_colour='')
```

#### Example 1

```python
from thumb_gen import Generator

app = Generator(video_path="C:/input/video.mp4",
                output_path="C:/output/",
                custom_text="www.example.com",
                font_dir="C:/Windows/Fonts/Arial.ttf",
                font_size=30)
app.run()
```

#### Example 2

```Python
import os
from thumb_gen import Generator

folder = 'C:/input'
for video in os.listdir(folder):
    if video.endswith('.mp4') or video.endswith('.mkv'):
        app = Generator(video_path=os.path.join(folder, video),
                        custom_text=False,
                        font_dir="C:/Project/font.ttf",
                        font_size=25,
                        bg_colour='blue',
                        font_colour='red')
        app.run()
```

#### Example 3

```Python
import os
from thumb_gen import Generator

folder = 'C:/input'
for video in os.listdir(folder):
    if video.endswith('.mp4') or video.endswith('.mkv'):
        app = Generator(video_path=os.path.join(folder, video),
                        columns=5,
                        rows=10,
                        custom_text=False,
                        font_dir="C:/Project/font.ttf",
                        font_size=25,
                        bg_colour='blue',
                        font_colour='red')
        app.run()
```
