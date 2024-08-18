import os
from googleapiclient.discovery import build
from flask import Flask, render_template, request, redirect, url_for
from media_services.download_media import DownloadMedia
from media_services.download_music import DownloadMusic


app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

youtube = build('youtube', 'v3', developerKey=API_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the index page and handles form submissions.

    On a GET request, renders the index.html template.
    On a POST request, checks if the user has initiated a search or download action.
    - If 'search' is in the form data, redirects to the search page.
    - If 'download' is in the form data, retrieves the provided URL and media type,
      then redirects to the format selection page.

    Returns:
        The rendered template for the index page or a redirect to another route.
    """
    if request.method == 'POST':
        if 'search' in request.form:
            return redirect(url_for('search'))
        if 'download' in request.form:
            url = request.form.get('url')
            media_type = request.form.get('media_type')
            if url:
                return redirect(url_for('select_format', url=url, media_type=media_type))
    return render_template('index.html')


@app.route('/select_format', methods=['GET', 'POST'])
def select_format():
    """
    Handles the format selection for media downloads.

    On a GET request, retrieves the media URL and type from the query parameters,
    initializes a DownloadMedia object, and gets available formats.
    On a POST request, handles the user's format selection and initiates the download.

    Returns:
        The rendered template for format selection, or the result after downloading the media.
    """
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
    """
    Handles searching for music videos on YouTube.

    On a POST request, retrieves the search query from the form, performs a YouTube search,
    and displays the list of videos that match the search criteria.

    Returns:
        The rendered template for the search form or the list of search results.
    """
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
    """
    Handles the download of audio from a selected YouTube video.

    On a POST request, retrieves the video ID from the form data, constructs the YouTube URL,
    and uses the DownloadMusic class to download the audio. The result is displayed on a result page.

    Returns:
        The rendered template for displaying the download result.
    """
    video_id = request.form['video_id'] 
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    downloader = DownloadMusic(url)
    file_path = downloader.download_audio()
    
    return render_template('result.html', message=file_path)




if __name__ == "__main__":
    app.run(debug=True)

