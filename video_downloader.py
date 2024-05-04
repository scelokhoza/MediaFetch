from pytube import YouTube
import os



# stream = YouTube(self.url).streams.get_by_resolution(resolution=chosen_resolution)
    
#     if stream:
#         # If the stream exists, download it
#         stream.download(output_path=self.download_path)
#         print(f"Downloaded {self.url} to {self.download_path}")
#     else:
#         # If the stream doesn't exist, inform the user
#         print(f"No stream available for {chosen_resolution}")



class DownloadVideo:
    def __init__(self, url)-> None:
        self.url = url
        self.download_path: str = os.path.join(os.path.expanduser('~'), 'Downloads')
        
    
    def get_videos_only(self) -> list:
        """
        This method fetches the video streams from the YouTube URL.

        Args:
        self (DownloadVideo): An instance of the DownloadVideo class.

        Returns:
        list: A list of video streams available for download.

        Raises:
        ConnectionError: If there is a problem with the internet connection.

        Example:
        >>> video_streams = download_video_obj.get_videos_only()
        """

        try:
            yt = YouTube(self.url)
            videos: list = yt.streams.filter(mime_type="video/mp4" ,adaptive=True).order_by('resolution').desc()
            return videos
        except ConnectionError:
            print("Connection Error, check your internet connection!!")
            return []
    
    
    def display_resolution_options(self, videos):
        """
        This method displays the available video resolutions for download.

        Args:
        self (DownloadVideo): An instance of the DownloadVideo class.

        Returns:
        None

        Example:
        >>> download_video_obj.display_resolution_options()
        """
        for i, video in enumerate(videos):
            # stream = YouTube(self.url).streams.get_by_resolution(resolution=video.resolution)
            # if stream:
            if self.is_downloadable(video):
                print(f"{i+1}. {self.filter_string(video)} DOWNLOAD")
            else:
                print(f"{i+1}. {self.filter_string(video)} NOT AVAILABLE")
            
    
    def is_downloadable(self, stream_object: object) -> bool:
        """
        This function checks if the stream is downloadable.

        Args:
        stream_object (object): The stream object obtained from the YouTube object.

        Returns:
        bool: True if the stream is downloadable, False otherwise.

        Example:
        >>> is_downloadable(stream_object)
        True
        """
        stream = YouTube(self.url).streams.get_by_resolution(resolution=stream_object.resolution)
        if stream:
            return True
        return 
    
    
    def filter_string(self, video_info) -> str:
        """
        This function filters the video information string to extract the resolution details.

        Args:
        video_info (str): The video information string obtained from the YouTube object.

        Returns:
        str: A string containing the video resolution in the format "widthxheight" and the video format "video/format".

        Example:
        >>> video_info = "video/mp4;abr=128000,res=1280x720"
        >>> filter_string(video_info)
        'video/mp4' '1280x720'
        """
        return video_info.mime_type + "  "+ video_info.resolution       
    
    
    def select_resolution_option(self, videos: list):
        """
        This method prompts the user to select a video resolution for download.

        Args:
        self (DownloadVideo): An instance of the DownloadVideo class.

        Returns:
        int: The user's selected video resolution index.

        Raises:
        ValueError: If the user enters an invalid number.

        Example:
        >>> download_video_obj.select_resolution_option()
        Enter the number of the resolution you want: 2
        2
        """
        self.display_resolution_options(videos)
        while True:
            try:
                resolution_option = int(input("Enter the number of the resolution you want: "))
                if resolution_option in range(1, len(videos) + 1):
                    return resolution_option
                else:
                    print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")
                
    
    def download_video(self):
        """
        This method downloads the selected video from the YouTube URL to the specified download path.

        Args:
        self (DownloadVideo): An instance of the DownloadVideo class.

        Returns:
        None

        Raises:
        ValueError: If the user enters an invalid number for selecting a resolution.

        Example:
        >>> download_video_obj.download_video()
        """
        videos = self.get_videos_only()
        resolution_option = self.select_resolution_option(videos)
        video = videos[resolution_option - 1]
        if self.is_downloadable(video):
            YouTube(self.url).streams.get_by_resolution(resolution=video.resolution).download(output_path=self.download_path)
            print(f"Downloaded {self.url} to {self.download_path}")
        else:
            print(f"No stream available for {self.filter_string(video)}")
        


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=42iQKuQodW4"
    download_video_obj = DownloadVideo(url)
    download_video_obj.download_video()