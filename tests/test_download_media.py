import unittest
from unittest.mock import patch, MagicMock
from media_services.download_media import DownloadMedia



class TestMediaDownload(unittest.TestCase):
        
    @patch('yt_dlp.YoutubeDL')
    def test_formats_audio(self, MockYoutubeDL):
        
        self.url = 'https://www.youtube.com/watch?v=is9hkpE-rlE'
        self.downloader = DownloadMedia(self.url)
        
        mock_info_dict: dict = {
            'formats': [
                {'acodec': 'mp3', 'filesize': 1000, 'ext': 'mp3'},
                {'acodec': 'none', 'filesize': 2000, 'ext': 'webm'},
                {'acodec': 'aac', 'filesize_approx': 3000, 'ext': 'aac'}
            ]
        }
        
        mock_ydl = MockYoutubeDL.return_value.__enter__.return_value
        mock_ydl.extract_info.return_value = mock_info_dict

        formats = self.downloader.get_formats('audio')

        self.assertEqual(len(formats), 2)
        self.assertEqual(formats[0]['acodec'], 'mp3')
        self.assertEqual(formats[1]['acodec'], 'aac')
        

if __name__ == '__main__':
    unittest.main()