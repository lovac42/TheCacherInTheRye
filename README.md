# The Cacher In The Rye (for Windows)

<i>An addon that caches audios coming through the rye...</i>

## About:
As it turns out, on windows, mplayer can't access files directly, so it gets copied to a temp directory first. Every time you click the replay button, it makes a copy. Unlike Unix, Windows flushes temp files immediately to the drive. So if you press the replay key 5 times on 300 cards each, that's 1500 temp files created per day, a quick way to kill off your SSD.

This addon keeps track of media files that are already played preventing multiple copies of the same file from being written to disk, speeding up access.

## Version:
This is the old branch that works with Anki up to v2.0.52 and v2.1.16.

The code in anki.sound has been moved to aqt.sound starting in v2.1.17 and will not work with this branch.
