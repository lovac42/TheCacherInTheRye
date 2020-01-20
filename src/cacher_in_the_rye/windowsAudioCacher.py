# -*- coding: utf-8 -*-
# Copyright 2018-2020 Lovac42
# Copyright 2006-2020 Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/TheCacherInTheRye


import os, random
from anki.hooks import addHook
from anki.utils import tmpdir


try:
    #test if v2.1.17++
    from aqt.sound import _player
    #actual import
    import aqt.sound as s
except ImportError:
    #old anki v2.1.16 or older
    import anki.sound as s


from .config import Config
from .test import selfTest
DEV_MODE = os.getenv("ANKIDEV", "")
ADDON_NAME = "CACHER_IN_THE_RYE"
conf = Config(ADDON_NAME)


audio_cached={}
def onShowQuestion(): #Clears cache on new Q
    global audio_cached
    limit=conf.get("cache_size", 64)
    if limit and len(audio_cached)>limit:
        audio_cached={}

if not conf.get("direct_access_mode", False):
    addHook('showQuestion', onShowQuestion)



#FROM: aqt.sound.queueMplayer v2.1.19 SRC
#MODS: added cacher
def queueMplayerWithCache(path):
    if DEV_MODE:
        selfTest()

    s.ensureMplayerThreads()
    if conf.get("direct_access_mode", False):
        # Modern versions of mplayer seems to have this unicode bug fixed.
        path=path.replace("\\", "/")
    elif os.path.exists(path):
        if path in audio_cached:
            path=audio_cached[path]
        else:
            # mplayer on windows doesn't like the encoding, so we create a
            # temporary file instead. oddly, foreign characters in the dirname
            # don't seem to matter.
            key=path
            dir = tmpdir()
            name = os.path.join(dir, "audio%s%s" % (
                random.randrange(0, 1000000), os.path.splitext(path)[1]))
            f = open(name, "wb")
            f.write(open(path, "rb").read())
            f.close()
            # it wants unix paths, too!
            path = name.replace("\\", "/")
            audio_cached[key]=path

    s.mplayerQueue.append(path)
    s.mplayerEvt.set()

s._player = queueMplayerWithCache
