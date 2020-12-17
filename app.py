from flask import Flask, render_template
import youtube_dl

app = Flask(__name__)

@app.route('/')
def hello():
    url = 'https://www.youtube.com/watch?v=kOZoLTQzpfg'

    ydl = youtube_dl.YoutubeDL({})
    with ydl:
        video = ydl.extract_info(url, download=False)
    # print('{} - {}'.format(video['artist'], video['track']))
    # https://colorpalettes.net/color-palette-4221/

    # return render_template('main.html', artist=video['artist'], song=video['track'])
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)