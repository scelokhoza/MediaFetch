import os
from googleapiclient.discovery import build
from media_services.download_media import DownloadMedia
from media_services.download_music import DownloadMusic
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)


API_KEY = os.getenv('API_KEY')

youtube = build('youtube', 'v3', developerKey=API_KEY)
        

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'search' in request.form:
            return redirect(url_for('search'))
        elif 'download' in request.form:
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


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            search_request = youtube.search().list(
                part="snippet",
                q=query,
                maxResults=5,
                type="video",
                videoCategoryId="10" 
            )
            response = search_request.execute()

            videos = []
            for item in response['items']:
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                videos.append({'title': title, 'video_id': video_id})

            return render_template('music_list.html', videos=videos)
    return render_template('search.html')


@app.route('/handle_button', methods=['POST'])
def handle_button():
    video_id = request.form['video_id'] 
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    downloader = DownloadMusic(url)
    file_path = downloader.download_audio()
    
    return render_template('result.html', message=file_path)



if __name__ == "__main__":
    app.run(debug=True)

