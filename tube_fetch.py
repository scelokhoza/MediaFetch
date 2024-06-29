from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

class DownloadAudio:
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
        
    def get_audios_only(self):
        try:
            yt = YouTube(self.url)
            audios = yt.streams.filter(mime_type="audio/mp4", adaptive=True).order_by('abr').desc()
            return audios
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def is_downloadable(self, stream_object):
        stream = YouTube(self.url).streams.get_by_itag(stream_object.itag)
        return stream is not None

    def filter_string(self, audio_info):
        return f"{audio_info.mime_type} {audio_info.abr}"
    
    def display_average_bitrate(self, audios):
        for i, audio in enumerate(audios):
            if self.is_downloadable(audio):
                print(f"{i+1}. {self.filter_string(audio)} DOWNLOAD")
            else:
                print(f"{i+1}. {self.filter_string(audio)} NOT AVAILABLE")
                
    def select_average_bitrate(self, audios):
        self.display_average_bitrate(audios)
        while True:
            try:
                bitrate_option = int(input("Enter the number of the bitrate you want to download: "))
                if bitrate_option in range(1, len(audios) + 1):
                    return bitrate_option
                else:
                    print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")
    
    def download_video(self, resolution):
        try:
            yt = YouTube(self.url)
            video = yt.streams.filter(res=resolution).first()
            if video:
                video.download(output_path=self.download_path)
                return f"Downloaded {self.url} video to {self.download_path}"
            else:
                return f"No stream available for video resolution {resolution}"
        except Exception as e:
            return f"Error: {e}"
    
    def download_audio(self, bitrate):
        try:
            yt = YouTube(self.url)
            audio = yt.streams.filter(abr=bitrate).first()
            if audio:
                audio.download(output_path=self.download_path)
                return f"Downloaded {self.url} audio to {self.download_path}"
            else:
                return f"No stream available for audio bitrate {bitrate}"
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
    download_audio_obj = DownloadAudio(url)
    videos = download_audio_obj.get_videos_only()
    audios = download_audio_obj.get_audios_only()
    
    if request.method == 'POST':
        if 'video_resolution' in request.form:
            resolution = request.form.get('video_resolution')
            message = download_audio_obj.download_video(resolution)
            return render_template('result.html', message=message)
        elif 'audio_bitrate' in request.form:
            bitrate = request.form.get('audio_bitrate')
            message = download_audio_obj.download_audio(bitrate)
            return render_template('result.html', message=message)
    
    return render_template('select_format.html', videos=videos, audios=audios, url=url)

if __name__ == "__main__":
    app.run(debug=True)

