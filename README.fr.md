# Détecteur de copyright des playlists sur YouTube

*Lire ceci en : [English](README.md)*

Cette une application web Flask qui utilise [youtube_dl](https://pypi.org/project/youtube_dl/) pour vérifier une playlist YouTube et rechercher tout copyright évident. Vous pouvez la trouver [ici](https://ytplaylist-copyright.herokuapp.com/).

Pour ce faire, elle utilise la section "Music in this video" de YouTube, située au bas de la description de la vidéo.

![Image montrant la section "Musique dans cette vidéo" de la description](/static/img/musicinvideo.PNG)

Évidemment, ce n'est pas sans défaut, mais c'est un façon rapide de vérifier si une playlist a une chanson dont le copyright est appliqué par un label de musique.
