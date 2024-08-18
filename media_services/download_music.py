import os
import yt_dlp

class DownloadMusic:
    """
    A class to handle downloading audio from a given URL using yt-dlp.

    Attributes:
        url (str): The URL of the media to download.
        download_path (str): The path where downloaded media will be saved.

    Methods:
        get_audios_only() -> list:
            Retrieves available audio formats for the given URL, filtering out formats
            that do not have a valid audio codec, size, or are in 'webm' format.

        select_average_bitrate(audios) -> dict:
            Selects the audio format with the highest average bitrate from a list of available audio formats.

        is_downloadable(audio) -> bool:
            Checks if the given audio format is valid and downloadable.

        download_audio() -> str or None:
            Downloads the audio format with the highest average bitrate and saves it to the specified download path.
            Returns the file path of the downloaded media if successful, or None if an error occurs.
    """

    def __init__(self, url) -> None:
        """
        Initializes the DownloadMusic instance with the specified URL.

        Args:
            url (str): The URL of the media to be downloaded.
        """
        self.url = url
        self.download_path: str = os.path.join(os.path.expanduser('~'), 'Downloads')

    def get_audios_only(self) -> list:
        """
        Retrieves available audio formats for the given URL.

        Filters the formats to include only those with a valid audio codec, file size,
        and excludes formats in 'webm' format.

        Returns:
            list: A list of available audio formats meeting the criteria.
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'extract_flat': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.url, download=False)
            formats = info_dict.get('formats', [])
            formats = [
                f for f in formats
                if f.get('acodec') != 'none'
                and f.get('acodec') is not None
                and (f.get('filesize') or f.get('filesize_approx'))
                and 'webm' not in f.get('ext', '')
            ]
            return formats

    def select_average_bitrate(self, audios):
        """
        Selects the audio format with the highest average bitrate.

        Args:
            audios (list): A list of available audio formats.

        Returns:
            dict: Audio format with the highest av bitrate, or None if no formats available.
        """
        if not audios:
            return None
        return max(audios, key=lambda x: int(x.get('abr') or 0))

    def is_downloadable(self, audio) -> bool:
        """
        Checks if the given audio format is valid and downloadable.

        Args:
            audio (dict): The audio format to check.

        Returns:
            bool: True if the audio format is valid and downloadable, False otherwise.
        """
        return audio is not None

    def download_audio(self):
        """
        Downloads the audio format with the highest average bitrate.

        Saves the downloaded media to the specified download path.

        Returns:
            str: The file path of the downloaded media if successful.
            None: If an error occurs during the download process or if no valid format is available.
        """
        audios = self.get_audios_only()
        audio = self.select_average_bitrate(audios)
        if self.is_downloadable(audio):
            ydl_opts = {
                'format': f'{audio["format_id"]}/bestaudio',
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'quiet': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    result = ydl.extract_info(self.url, download=True)
                    file_path = ydl.prepare_filename(result)
                    return f"Downloaded media to {file_path}"
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None
        else:
            return None


if __name__ == '__main__':
    downloader = DownloadMusic("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
    downloader.download_audio()




