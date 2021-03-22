# Thumbnail Generator 🎬

[![Build Status](https://travis-ci.com/truethari/thumb-gen.svg?branch=master)](https://travis-ci.com/truethari/thumb-gen)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/01b66feeb94743ac80e413e4e9075595)](https://www.codacy.com/gh/truethari/thumb-gen/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=truethari/thumb-gen&amp;utm_campaign=Badge_Grade)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://badge.fury.io/py/thumb-gen.svg)](https://badge.fury.io/py/thumb-gen)

## What is This

--------
This is a Python application that can be used to generate video thumbnail for mp4 and mkv file types.

[![Imgur](https://i.imgur.com/Yq9roDT.png)](https://imgur.com/Yq9roDT)

## Installation

You can use pip:

```console
~$ pip3 install thumb-gen
```

## Configurations

(These may change during the update)

-  The number of screen images that should be included in the final thumbnail image.

-  Thumbnail image quality

-  Font type in the video info panel. You can add a file path of a font file (.ttf) to this.

-  Font size in the video info panel

- Custom text in the video info panel

``` console
~$ thumb-gen -c
```

or

``` console
~$ thumb-gen --config
```

By program default:

``` ini
IMAGES = 12
IMAGE_QUALITY = 100
FONT = arial.ttf
FONT_SIZE = 30
CUSTOM_TEXT = ''
```

## Usage options

``` text
-h, --help      show this help message and exit

-c, --config    change screenshots for thumbnail image and image quality

-v, --version   show program's version number and exit

-f, --file      input a single video

-w, --where     input a single video from another directory

-d, --dir       input videos from a directory
```

## Usage

Example

``` console
~$ thumb-gen -h
~$ thumb-gen --help

~$ thumb-gen -c
~$ thumb-gen --config

~$ thumb-gen -v
~$ thumb-gen --version

~$ thumb-gen -f input.mp4
~$ thumb-gen --file input.mp4

~$ thumb-gen -w "D:/Videos/input.mp4"
~$ thumb-gen --where "D:/Videos/input.mp4"

~$ thumb-gen -d videos
~$ thumb-gen --dir videos
```
