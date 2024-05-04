import unittest
from unittest.mock import patch
from video_downloader import DownloadVideo


class TestDownloadVideo(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.youtube.com/watch?v=OpohbXB_JZU"
        self.download_video = DownloadVideo(self.url)
        
        
    def test_get_videos_only(self):
        with patch('pytube.YouTube.streams', return_value=[]) as mock_streams:
            self.assertEqual(self.download_video.get_videos_only(), [])
            
            
    def test_display_resolution_options(self):
        with patch('pytube.YouTube.streams', return_value=[]) as mock_streams:
            self.download_video.display_resolution_options()
    
    
    def test_select_resolution_option(self):
        with patch('pytube.YouTube.streams', return_value=[]) as mock_streams:
            self.download_video.select_resolution_option()
            
    
    def test_download_video(self):
        with patch('pytube.YouTube.streams', return_value=[]) as mock_streams:
            self.download_video.download_video()
            
    
    def test_select_resolution_option(self):
        self.assertEqual(self.download_video.select_resolution_option(), 1)

        with self.assertRaises(ValueError):
            self.download_video.select_resolution_option("a")

        with self.assertRaises(ValueError):
            self.download_video.select_resolution_option(5)