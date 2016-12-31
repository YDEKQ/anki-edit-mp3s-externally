# -*- mode: Python ; coding: utf-8 -*-

# This add on adds a button to the add/editor window that, when clicked, opens up all images in the note in whatever image editor you have set to default in OSx. 
# This is basically a clone of Dimitry Mikheev's "Edit Audio Images" add on (https://ankiweb.net/shared/info/1075177705) with a few work arounds to get it working in Mac OSx.
# There is no shortcut key to open the file, you must click a button in the editor.
# If there is any issues with it, please let me know and I will try my best to fix them. That being said, I have never used python before and I might not be able to fix any bugs!
# https://github.com/carlseverson/anki-edit-images-externally

# • Edit Audio Images
# https://ankiweb.net/shared/info/1040866511
# https://github.com/ankitest/anki-musthave-addons-by-ankitest
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Copyright (c) 2016 Dmitry Mikheev, http://finpapa.ucoz.net/
#
# In card reviewer F10 opens all sounds and images in external editors.
# In Add/Edit window F10 opens sounds and images only from current field.
#
# No support. Use it AS IS on your own risk.




# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

#import regular expressions
import re
import os
from anki.hooks import addHook
from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showInfo

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def editMp3Externally():
    fields = mw.reviewer.card.note().fields
    #iterate through things and find all .mp3 files
    for field in fields:
        sounds = re.findall(r'\[sound:(.*?)\]', field)
        pathToCollection = mw.col.media.dir() +"/"
        for sound in sounds:
            if sound:
                fullPath = os.path.join(pathToCollection,sound)
                fullPath = re.sub(" ","\ ",fullPath)
                os.system("open -a " + "\'Audacity\'" + " " + fullPath)
 

def buttonPressed(self):
    editMp3Externally()

def mySetupButtons(self):
    # - size=False tells Anki not to use a small button
    # - the lambda is necessary to pass the editor instance to the
    #   callback, as we're passing in a function rather than a bound
    #   method
    self._addButton("mybutton", lambda s=self: buttonPressed(self),
                    text="Edit mp3s", size=False, tip="Edit mp3s in OSx's default external editor.")

Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
