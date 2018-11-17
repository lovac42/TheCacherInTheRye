# TheCacherInTheRye
AnkiAddon: Caches Audio Files on Windows

## About:
<i>An addon that caches audios coming through the rye...</i>

As it turns out, on windows, mplayer can't access files directly, so it gets copied to the temp directory first. Every time you click the replay button, it makes a temp copy. Unlike Unix, Windows flushes temp files immediately to the drive. So if you click the replay key 5 times on 300 cards each, that's 1500 temp files created per day, a quick way to kill off your SSD.

This addon keeps track of audio files that are already cached preventing multiple copies of the same file from being written to disk, speeding up access.

