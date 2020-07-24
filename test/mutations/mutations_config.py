import pytest_mutagen as mg
import h2
from h2.config import _BooleanConfigOption, H2Configuration

mg.link_to_file(mg.APPLY_TO_ALL)

#hash=a7208433e593efdf
@mg.mutant_of("_BooleanConfigOption.__init__", "_BOOLEANCONFIGOPTION.__INIT___0")
def __init__(self, name):
    self.name = None
    self.attr_name = '_%s' % self.name

#hash=6d170904a33f506c
@mg.mutant_of("_BooleanConfigOption.__init__", "_BOOLEANCONFIGOPTION.__INIT___1")
def __init__(self, name):
    self.name = name
    self.attr_name = None

