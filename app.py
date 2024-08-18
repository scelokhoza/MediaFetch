from flask import Flask, render_template, request, redirect, url_for
from media_services.download_media import DownloadMedia



app = Flask(__name__)


# AIzaSyA183e8JN05L1A3IFBVtxTtHNk7jKsL2iI
        

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

