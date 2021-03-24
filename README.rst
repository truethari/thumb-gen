===================
Thumbnail Generator
===================

.. image:: https://travis-ci.com/truethari/thumb-gen.svg?branch=master
   :target: https://travis-ci.com/truethari/thumb-gen
.. image:: https://app.codacy.com/project/badge/Grade/01b66feeb94743ac80e413e4e9075595
   :target: https://www.codacy.com/gh/truethari/thumb-gen/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=truethari/thumb-gen&amp;utm_campaign=Badge_Grade

-------------
What is This?
-------------
This is a Python application that can be used to generate video thumbnail for mp4 and mkv file types.

.. image:: https://i.imgur.com/Yq9roDT.png
   :target: https://github.com/truethari/thumb-gen

------------
Installation
------------

You can use pip:

.. code-block:: bash

   ~$ pip3 install thumb-gen

--------------
Configurations
--------------

(These may change during the update)

- The number of screen images that should be included in the final thumbnail image.

- Thumbnail image quality

- Font type in the video info panel. You can add a file path of a font file (.ttf) to this.

- Font size in the video info panel

- Custom text in the video info panel

.. code-block:: bash

   ~$ thumb-gen -c

or

.. code-block:: bash

   ~$ thumb-gen --config

By program default:

.. code-block:: ini

   IMAGES = 12
   IMAGE_QUALITY = 100
   FONT = arial.ttf
   FONT_SIZE = 30
   CUSTOM_TEXT = ''

-----
Usage 
-----
Usage options:
==============

.. code-block::

   -h, --help      show this help message and exit

   -c, --config    change screenshots for thumbnail image and image quality

   -v, --version   show program's version number and exit

   -f, --file      input a single video

   -d, --dir       input videos from a directory

Console
========

.. code-block:: bash

   ~$ thumb-gen -h
   ~$ thumb-gen --help

   ~$ thumb-gen -c
   ~$ thumb-gen --config

   ~$ thumb-gen -v
   ~$ thumb-gen --version

   ~$ thumb-gen -f input.mp4
   ~$ thumb-gen --file input.mp4
   ~$ thumb-gen --file "d:/videos/input.mp4"

   ~$ thumb-gen -d videos
   ~$ thumb-gen --dir videos

Python
======

- If you don't set an output folder, thumbnail images will be saved in the video folder (video_path).

- If you don't need a custom text and you have already set a custom text for the configuration file (using console), it will be added automatically. To avoid this set the `custom_text` value to `False` .

Example 1

.. code-block:: Python

   from thumb_gen import worker

   #video_path, output_path='', custom_text=True
   app = worker.Generator("C:/input/video.mp4", "C:/output/", "www.example.com")
   app.run()

Example 2

.. code-block:: Python

   import os
   from thumb_gen import worker
   
   folder = 'C:/input/'
   for video in os.listdir(folder):
       if video.endswith('.mp4') or video.endswith('.mkv'):
           app = worker.Generator((folder + video), custom_text=False)
           app.run()
