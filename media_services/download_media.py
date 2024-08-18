import os
import yt_dlp


class DownloadMedia:
    """
    A class to handle downloading media from a given URL using yt-dlp.

    Attributes:
        url (str): The URL of the media to download.
        download_path (str): The path where downloaded media will be saved.
    """

    def __init__(self, url) -> None:
        """
        Initializes the DownloadMedia instance with the specified URL.

        Args:
            url (str): The URL of the media to be downloaded.
        """
        self.url = url
        self.download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    def get_formats(self, media_type):
        """
        Retrieves available formats for the specified media type (audio or video).

        Args:
            media_type (str): The type of media to retrieve formats for.
                              Should be 'audio' or 'video'.

        Returns:
            list: A list of formats that are available for download, filtered to include
                  only those with a file size and excluding 'webm' formats.
        """
        ydl_opts = {
            'listformats': True,
            'quiet': True
        }
        formats = []
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=False)
                formats = info_dict.get('formats', [])

                if media_type == 'audio':
                    formats = [
                        f for f in formats
                        if f.get('acodec') != 'none'
                        and f.get('acodec') is not None
                        and (f.get('filesize') or f.get('filesize_approx'))
                        and 'webm' not in f.get('ext', '')
                    ]
                else:
                    formats = [
                        f for f in formats
                        if f.get('vcodec') != 'none'
                        and f.get('vcodec') is not None
                        and (f.get('filesize') or f.get('filesize_approx'))
                        and 'webm' not in f.get('ext', '')
                    ]
        except Exception as e:
            return f"Error: {e}"
        return formats


    def download_media(self, format_id):
        """
        Downloads the media using the specified format ID.

        Args:
            format_id (str): The format ID of the media to download.

        Returns:
            str: A message indicating the download status, including the download path
                 or an error message if the download fails.
        """
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



if __name__ == "__main__":
    downloader = DownloadMedia('https://www.youtube.com/watch?v=is9hkpE-rlE')
    print(downloader.get_formats('audio'))