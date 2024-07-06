# import unittest
# from unittest.mock import patch, MagicMock
# from download_media import DownloadMedia

# class TestDownloadVideo(unittest.TestCase):

#     def setUp(self):
#         self.x_url = "https://x.com/Unexplainvideo/status/1805937364256293119"
#         self.youtube_url: str
#         self.instagram_url: str
#         self.linkedin_url: str
#         self.tiktok_url: str
#         self.download_video = DownloadMedia(self.x_url)

#     @patch('yt_dlp.YoutubeDL')
#     def test_get_videos_only(self, mock_yt_dlp):
#         # Mock the YoutubeDL instance and its methods
#         mock_ydl_instance = MagicMock()
#         mock_yt_dlp.return_value.__enter__.return_value = mock_ydl_instance
#         mock_ydl_instance.extract_info.return_value = {
#             'formats': [{'format_id': '18', 'ext': 'mp4'}]
#         }

#         formats = self.download_video.get_videos_only()
#         self.assertEqual(len(formats), 1)
#         self.assertEqual(formats[0]['format_id'], '18')

#     @patch('yt_dlp.YoutubeDL')
#     @patch('os.path.join', return_value='/mock/path/video.mp4')
#     def test_download_video(self, mock_path_join, mock_yt_dlp):
#         # Mock the YoutubeDL instance and its methods
#         mock_ydl_instance = MagicMock()
#         mock_yt_dlp.return_value.__enter__.return_value = mock_ydl_instance

#         format_id = '18'
#         message = self.download_video.download_video(format_id)
#         self.assertIn("Downloaded video to", message)

#     @patch('yt_dlp.YoutubeDL')
#     def test_get_videos_only_exception(self, mock_yt_dlp):
#         # Mock the YoutubeDL instance to raise an exception
#         mock_ydl_instance = MagicMock()
#         mock_yt_dlp.return_value.__enter__.return_value = mock_ydl_instance
#         mock_ydl_instance.extract_info.side_effect = Exception("Test Exception")

#         formats = self.download_video.get_videos_only()
#         self.assertEqual(formats, [])

#     @patch('yt_dlp.YoutubeDL')
#     def test_download_video_exception(self, mock_yt_dlp):
#         # Mock the YoutubeDL instance to raise an exception
#         mock_ydl_instance = MagicMock()
#         mock_yt_dlp.return_value.__enter__.return_value = mock_ydl_instance
#         mock_ydl_instance.download.side_effect = Exception("Test Exception")

#         format_id = '18'
#         message = self.download_video.download_video(format_id)
#         self.assertIn("Error:", message)

# if __name__ == '__main__':
#     unittest.main()