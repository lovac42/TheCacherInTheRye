# The Cacher In The Rye (for Windows)

https://ankiweb.net/shared/info/1302452246

<i>An addon that caches audios coming through the rye...</i>

## About:
As it turns out, on windows, mplayer can't access files directly, so it gets copied to a temp directory first. Every time you click the replay button, it makes a copy. Unlike Unix, Windows flushes temp files immediately to the drive. So if you press the replay key 5 times on 300 cards each, that's 1500 temp files created per day, a quick way to kill off your SSD.

This addon keeps track of audio files that are already played preventing multiple copies of the same file from being written to disk, speeding up access.
