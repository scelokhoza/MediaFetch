from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

class DownloadMedia:
    def __init__(self, url):
        self.url = url
        self.download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
    def get_videos_only(self):
        ydl_opts = {
            'listformats': True,
            'quiet': True
        }
        formats = []
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=False)
                formats = info_dict.get('formats', [])
        except Exception as e:
            print(f"Error: {e}")
        return formats

    def download_video(self, format_id):
        ydl_opts = {
            'format': format_id,
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s')
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            return f"Downloaded video to {self.download_path}"
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
    download_video_obj = DownloadMedia(url)
    formats = download_video_obj.get_videos_only()
    if request.method == 'POST':
        format_id = request.form.get('format_id')
        message = download_video_obj.download_video(format_id)
        return render_template('result.html', message=message)
    return render_template('select_format.html', formats=formats, url=url)


if __name__ == "__main__":
    app.run(debug=True)
