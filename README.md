# The Cacher In The Rye (for Windows)


## Obsolete:
This addon works upto version 2.1.19. It is no longer necessary for newer versions.

From Anki's changelogs for 2.1.20:
```
Anki now starts a new copy of mplayer for each audio file on Windows, which avoids the need to create temporary files.
```


## About:
<i>An addon that caches audios coming through the rye...</i>

As it turns out, on windows, mplayer can't access files directly, so it gets copied to a temp directory first. Every time you click the replay button, it makes a copy. Unlike Unix, Windows flushes temp files immediately to the drive. So if you press the replay key 5 times on 300 cards each, that's 1500 temp files created per day, a quick way to kill off your SSD.

This addon keeps track of media files that are already played preventing multiple copies of the same file from being written to disk, speeding up access.


## Demo:

<img src="https://github.com/lovac42/TheCacherInTheRye/blob/master/screenshots/demo.png?raw=true">  
