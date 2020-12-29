from os import error
from flask import Flask, render_template, request
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/videos', methods=['POST'])
def videos():
    url = request.form['link']

    #TODO Watch for privated or deleted videos
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
                copyrightedVideos.append([video['title'], video['artist'], video['track'], video['webpage_url'], video['thumbnail']])
        except error:
            print(error)

    return render_template('main.html', videos=copyrightedVideos, numCopy=len(copyrightedVideos), numTotal=len(videos))

if __name__ == '__main__':
    app.run(debug=True)