from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

class DownloadMedia:
    def __init__(self, url):
        self.url = url
        self.download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    def get_formats(self, media_type):
        ydl_opts = {
            'listformats': True,
            'quiet': True
        }
        formats = []
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=False)
                formats = info_dict.get('formats', [])
                print(f"Available formats for {media_type}: {formats}") 
                if media_type == 'audio':
                    formats = [f for f in formats if f.get('acodec') != 'none' and f.get('acodec') is not None and (f.get('filesize') or f.get('filesize_approx'))]
                else:  
                    formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('vcodec') is not None and (f.get('filesize') or f.get('filesize_approx'))]
                print(f"Filtered formats for {media_type}: {formats}") 
        except Exception as e:
            print(f"Error: {e}")
        return formats




    def download_media(self, format_id):
        ydl_opts = {
            'format': format_id,
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s')
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            return f"Downloaded media to {self.download_path}"
        except Exception as e:
            return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        media_type = request.form.get('media_type') 
        if url:
            return redirect(url_for('select_format', url=url, media_type=media_type))
    return render_template('index.html')

@app.route('/select_format', methods=['GET', 'POST'])
def select_format():
    url = request.args.get('url')
    media_type = request.args.get('media_type')  
    download_media_obj = DownloadMedia(url)
    formats = download_media_obj.get_formats(media_type)  
    if request.method == 'POST':
        format_id = request.form.get('format_id')
        message = download_media_obj.download_media(format_id)
        return render_template('result.html', message=message)
    return render_template('select_format.html', formats=formats, url=url, media_type=media_type)

if __name__ == "__main__":
    app.run(debug=True)

