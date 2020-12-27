from os import error
from flask import Flask, render_template, request
import youtube_dl, time, json, flask

app = Flask(__name__)

@app.route('/')
def index():
    # https://colorpalettes.net/color-palette-4221/
    return render_template('main.html')

@app.route('/process', methods=['POST'])
def process():
    # test - https://www.youtube.com/playlist?list=PLyEROMcux1lU6vV-axvuv52ldd5m3nwWG
    # real - https://www.youtube.com/playlist?list=PLyEROMcux1lW4ybgltuzB2W-cmzCViSpR
    # url = 'https://www.youtube.com/playlist?list=PLyEROMcux1lU6vV-axvuv52ldd5m3nwWG'
    url = request.form['link']

    # Extract videos from playlist and get info
    ydl = youtube_dl.YoutubeDL({})
    with ydl:
        extraction = ydl.extract_info(url, download=False)
        videos = extraction['entries']

    # Search videos for any obvious copyright
    copyrightedVideos = []
    for video in videos:
        try:
            if video['artist'] != None:
                copyrightedVideos.append([video['artist'], video['track'], video['webpage_url']])
        except error:
            print(error)

    # print(f'{len(copyrightedVideos)} out of {len(videos)} videos had obvious copyrighted music')
    # print(copyrightedVideos)
    return render_template('videos.html', videos=copyrightedVideos)

if __name__ == "__main__":
    app.run(debug=True)