import os
import yt_dlp

class DownloadMusic:
    def __init__(self, url) ->None:
        self.url = url
        self.download_path: str = os.path.join(os.path.expanduser('~'), 'Downloads')

    def get_audios_only(self) -> list:
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
            audio_formats = [f for f in formats]
            return audio_formats

    def select_average_bitrate(self, audios):
        if not audios:
            return None
        return max(audios, key=lambda x: int(x.get('abr') or 0))  

    def is_downloadable(self, audio) -> bool:
        return audio is not None

    def download_audio(self):
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



