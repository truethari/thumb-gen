import  pathlib

from    setuptools      import setup, find_packages

exec(open("thumb_gen/version.py").read())

here = pathlib.Path(__file__).parent
with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name="thumb_gen",
    version=__version__,
    description="Python application that can be used to generate video thumbnail for mp4 and mkv file types.",
    long_description=long_description,
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
    ],
    packages=['thumb_gen'],
    include_package_data=True,
    package_data = {'' : ['fonts/*.ttf']},
    install_requires=["Pillow", "get-video-properties", "ffmpy"],
    entry_points={
        "console_scripts": [
            "thumb-gen=thumb_gen.__main__:run",
        ]
    },
)
