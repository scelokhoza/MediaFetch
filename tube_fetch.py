from flask import Flask, render_template, request, jsonify
from video_downloader import DownloadVideo



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_formats', methods=['POST'])
def get_formats():
    url = request.form['url']
    download_video_obj = DownloadVideo(url)
    video_formats = download_video_obj.get_videos_only()
    return jsonify(video_formats)



@app.route('/download_video', methods=['POST'])
def download_video():
    url = request.form['url']
    download_video_obj = DownloadVideo(url)
    download_video_obj.download_video()
    return jsonify(True)


if __name__ == '__main__':
    app.run(debug=True)