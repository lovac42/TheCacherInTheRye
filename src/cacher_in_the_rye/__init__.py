# -*- coding: utf-8 -*-
# Copyright 2018-2020 Lovac42
# Copyright 2006-2020 Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/TheCacherInTheRye


from anki.utils import isWin

if isWin:
    from . import windowsAudioCacher
