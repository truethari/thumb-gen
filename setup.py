import pathlib

from setuptools import setup, find_packages
from thumb_gen  import __version__

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="thumb_gen",
    version=__version__,
    description="Python application that can be used to generate video thumbnail for mp4 and mkv file types.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/thumb-gen",
    keywords="thumbnails video screenshot",
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/truethari/thumb-gen/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=['thumb_gen'],
    include_package_data=True,
    package_data = {'' : ['fonts/*.ttf']},
    install_requires=["Pillow", "infomedia", "ffmpy"],
    entry_points={
        "console_scripts": [
            "thumb-gen=thumb_gen.__main__:main",
        ]
    },
)
