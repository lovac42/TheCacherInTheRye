@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=cacher_in_the_rye
set NAME=cacher_in_the_rye
set PACKID=1302452246
set VERSION=0.0.2


quick_manifest.exe "The Cacher In The Rye" "%PACKID%" >%REPO%\manifest.json
echo %VERSION% >%REPO%\VERSION

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%\checksum.md5

cd %REPO%
%ZIP% ../%NAME%_v%VERSION%_Anki21.ankiaddon *
