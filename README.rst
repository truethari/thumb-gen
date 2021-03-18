===================
Thumbnail Generator
===================

.. image:: https://travis-ci.com/truethari/thumb-gen.svg?branch=master
   :target: https://travis-ci.com/truethari/thumb-gen
.. image:: https://app.codacy.com/project/badge/Grade/01b66feeb94743ac80e413e4e9075595
   :target: https://www.codacy.com/gh/truethari/thumb-gen/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=truethari/thumb-gen&amp;utm_campaign=Badge_Grade

.. image:: https://socialify.git.ci/truethari/thumb-gen/image?description=1&descriptionEditable=Python%20application%20that%20can%20be%20used%20to%20generate%20video%20thumbnail%20for%20mp4%20and%20mkv%20file%20types.&font=Inter&language=1&logo=https%3A%2F%2Fen.gravatar.com%2Fuserimage%2F101097900%2F0187b63cf526a88a4c67cab4ab5bfe7f.png&owner=1&pattern=Circuit%20Board&theme=Dark
   :target: https://github.com/truethari/thumb-gen

-------------
What is This?
-------------
This is a Python application that can be used to generate video thumbnail for mp4 and mkv file types.

Configurations
==============

(These may change during the update)

- The number of screen images that should be included in the final thumbnail image.
- Thumbnail image quality

.. code-block:: bash

   ~$ thumb-gen -c

or

.. code-block:: bash

   ~$ thumb-gen --config


By program default:

.. code-block:: ini

   IMAGES = 12
   IMAGE_QUALITY = 100

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

   -w, --where     input a single video from another directory

   -d, --dir       input videos from a directory

Examples
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

   ~$ thumb-gen -w "D:/Videos/input.mp4"
   ~$ thumb-gen --where "D:/Videos/input.mp4"

   ~$ thumb-gen -d videos
   ~$ thumb-gen --dir videos
