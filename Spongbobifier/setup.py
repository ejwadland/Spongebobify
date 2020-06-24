from setuptools import setup

APP = ['Spongebobifier.py']
DATA_FILES = ['Spongebob.png']
OPTIONS = {'argv_emulation' : True}

setup(
    app = APP,
    data_files = DATA_FILES,
    options ={'py2app' : OPTIONS},
    setup_requires=['py2app'],
)