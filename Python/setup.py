#setup.py
from distutils.core import setup
import py2exe
filename = raw_input('File to be converted? ')
setup(console=[filename])
