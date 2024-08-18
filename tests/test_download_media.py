import unittest
from unittest.mock import patch
from media_services.download_media import DownloadMedia



class TestMediaDownload(unittest.TestCase):
        
    @patch('yt_dlp.YoutubeDL')
    def test_formats_audio(self, mock_youtube_dl):
        url = 'https://www.youtube.com/watch?v=is9hkpE-rlE'
        self.downloader = DownloadMedia(url)
        
        mock_info_dict: dict = {
            'formats': [
                {'acodec': 'mp3', 'filesize': 1000, 'ext': 'mp3'},
                {'acodec': 'none', 'filesize': 2000, 'ext': 'webm'},
                {'acodec': 'aac', 'filesize_approx': 3000, 'ext': 'aac'}
            ]
        }
        
        mock_ydl = mock_youtube_dl.return_value.__enter__.return_value
        mock_ydl.extract_info.return_value = mock_info_dict

        formats = self.downloader.get_formats('audio')

        self.assertEqual(len(formats), 2)
        self.assertEqual(formats[0]['acodec'], 'mp3')
        self.assertEqual(formats[1]['acodec'], 'aac')
        
    
    @patch('yt_dlp.YoutubeDL')
    def test_get_formats(self, mock_youtube_dl):
        url = 'https://www.tiktok.com/@polo_vivo1/video/7309428046522502405'
        self.downloader = DownloadMedia(url)
        
        mock_info_dict = {
            'formats': [
                {'vcodec': 'h264', 'filesize': 1000, 'ext': 'mp4'},
                {'vcodec': 'none', 'filesize': 2000, 'ext': 'webm'},
                {'vcodec': 'vp9', 'filesize_approx': 3000, 'ext': 'webm'}
            ]
        }
        mock_ydl = mock_youtube_dl.return_value.__enter__.return_value
        mock_ydl.extract_info.return_value = mock_info_dict

        formats = self.downloader.get_formats('video')

        self.assertEqual(len(formats), 1)
        self.assertEqual(formats[0]['vcodec'], 'h264')
        
    
    @patch('yt_dlp.YoutubeDL')
    def test_get_formats_error(self, mock_youtube_dl):
        url = 'https://www.tiktok.com/@polo_vivo1/video/7309428046522502405'
        self.downloader = DownloadMedia(url)
        
        mock_ydl = mock_youtube_dl.return_value.__enter__.return_value
        mock_ydl.extract_info.side_effect = Exception("Test error")

        result = self.downloader.get_formats('audio')
        self.assertEqual(result, "Error: Test error")
        
    
    @patch('yt_dlp.YoutubeDL')
    def test_get_formats_no_formats(self, mock_youtube_dl):
        url = 'https://www.youtube.com/watch?v=is9hkpE-rlE'
        self.downloader = DownloadMedia(url)
        
        mock_info_dict = {'formats': []}
        
        mock_ydl = mock_youtube_dl.return_value.__enter__.return_value
        mock_ydl.extract_info.return_value = mock_info_dict

        formats = self.downloader.get_formats('audio')

        self.assertEqual(formats, [])
        
        

if __name__ == '__main__':
    unittest.main()