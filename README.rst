===================
Thumbnail Generator
===================

-------------
What is This?
-------------
This is a Python application that can be used to generate video thumbnail for mp4 and mkv file types.

Configurations
==============
This application contains several default values that cannot be changed externally. You can modify **config.py** as follows.

(These may change during the update)

- The number of screen images that should be included in the final thumbnail image.
- Thumbnail image quality

.. code-block:: Python

   IMAGES = 12
   IMAGE_QUALITY = 100

-----
Usage 
-----
Usage options:
==============

.. code-block::

    -v, --version       show program's version number and exit
    -h, --help          show this help message and exit
    -w, --where         input a single video from another directory
    -f, --file          input a single video
    -d, --dir           input videos from a directory

Examples
========
.. code-block:: bash

   ~$ python main.py -h
   ~$ python main.py --help

   ~$ python main.py -v
   ~$ python main.py --version

   ~$ python main.py -f input.mp4
   ~$ python main.py --file input.mp4

   ~$ python main.py -w "D:/Videos/input.mp4"
   ~$ python main.py --where "D:/Videos/input.mp4"

   ~$ python main.py -d videos
   ~$ python main.py --dir videos