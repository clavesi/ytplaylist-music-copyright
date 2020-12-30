# YouTube Playlist Copyright Detector

*Read this in: [Français](README.fr.md)*

This is a Flask web app that uses [youtube_dl](https://pypi.org/project/youtube_dl/) to check a YouTube playlist and search for any obvious copyright. Find it [here](https://ytplaylist-copyright.herokuapp.com/).

This is done using YouTube's "Music in this video" section at the bottom of a video description.

![Image showing "Music in this video" section of description](/static/img/musicinvideo.PNG)

Of course this isn't flawless, but it's a quick way to check if a playlist has a song that's copyright is enforced by a music label.
