# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/TheCacherInTheRye
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1


#=== CONFIGS ===============================

#Resets cache when greater
MAX_CACHE_SIZE = 25

#=== END_CONFIGS ===========================
############################################


import anki, os
from anki.hooks import addHook
from anki.utils import tmpdir, isWin
from anki.sound import *

from anki import version
ANKI21 = version.startswith("2.1.")


audio_cached={}
def onShowQuestion(): #Clears cache on new Q
    global audio_cached
    if len(audio_cached)>MAX_CACHE_SIZE:
        audio_cached={}
addHook('showQuestion', onShowQuestion)



#From: anki.sound.queueMplayer v2.0.52 & v2.1.5 SRC
#Added: cacher
def queueMplayerWithCache(path):
    ensureMplayerThreads()
    if isWin and os.path.exists(path):
        # mplayer on windows doesn't like the encoding, so we create a
        # temporary file instead. oddly, foreign characters in the dirname
        # don't seem to matter.
        if path in audio_cached:
            path=audio_cached[path]
        else:
            key=path
            dir = tmpdir()
            name = os.path.join(dir, "audio%s%s" % (
                random.randrange(0, 1000000), os.path.splitext(path)[1]))
            f = open(name, "wb")
            f.write(open(path, "rb").read())
            f.close()
            # it wants unix paths, too!
            path = name.replace("\\", "/")
            if not ANKI21:
                path = path.encode(sys.getfilesystemencoding())
            audio_cached[key]=path
    elif not ANKI21:
        path = path.encode("utf-8")

    anki.sound.mplayerQueue.append(path)
    anki.sound.mplayerEvt.set()

anki.sound._player = queueMplayerWithCache
