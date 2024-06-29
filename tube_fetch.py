from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os


app = Flask(__name__)

class DownloadVideo:
    def __init__(self, url):
        self.url = url
        self.download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
    def get_videos_only(self):
        try:
            yt = YouTube(self.url)
            videos = yt.streams.filter(mime_type="video/mp4", adaptive=True).order_by('resolution').desc()
            return videos
        except Exception as e:
            print(f"Error: {e}")
            return []
        
    def is_downloadable(self, stream_object):
        stream = YouTube(self.url).streams.get_by_resolution(resolution=stream_object.resolution)
        return stream is not None

    def filter_string(self, video_info):
        return f"{video_info.mime_type} {video_info.resolution}"
    
    def download_video(self, resolution):
        try:
            yt = YouTube(self.url)
            video = yt.streams.filter(res=resolution).first()
            if video:
                video.download(output_path=self.download_path)
                return f"Downloaded {self.url} to {self.download_path}"
            else:
                return f"No stream available for resolution {resolution}"
        except Exception as e:
            return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            return redirect(url_for('select_format', url=url))
    return render_template('index.html')

@app.route('/select_format', methods=['GET', 'POST'])
def select_format():
    url = request.args.get('url')
    download_video_obj = DownloadVideo(url)
    videos = download_video_obj.get_videos_only()
    if request.method == 'POST':
        resolution = request.form.get('resolution')
        message = download_video_obj.download_video(resolution)
        return render_template('result.html', message=message)
    return render_template('select_format.html', videos=videos, url=url)

if __name__ == "__main__":
    app.run(debug=True)
