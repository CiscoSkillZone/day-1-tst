# Autodetecting setup.py script for building the Python extensions
#

__version__ = "$Revision$"

import sys, os, imp, re, optparse
from glob import glob
from platform import machine as platform_machine

from distutils import log
from distutils import sysconfig
from distutils import text_file
from distutils.errors import *
from distutils.core import Extension, setup
from distutils.command.build_ext import build_ext
from distutils.command.install import install
from distutils.command.install_lib import install_lib

# This global variable is used to hold the list of modules to be disabled.
disabled_module_list = []
