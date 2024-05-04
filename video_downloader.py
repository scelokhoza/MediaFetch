from pytube import YouTube
import os


# YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.get_by_resolution('7').



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
            videos: list = yt.streams.filter(mime_type="video/mp4" ,progressive=True)
            return videos
        except ConnectionError:
            print("Connection Error, check your internet connection!!")
            return []
    
    
    def display_resolution_options(self):
        """
        This method displays the available video resolutions for download.

        Args:
        self (DownloadVideo): An instance of the DownloadVideo class.

        Returns:
        None

        Example:
        >>> download_video_obj.display_resolution_options()
        """
        videos: list = self.get_videos_only()
        for i, video in enumerate(videos):
            print(f"{i+1}. {self.filter_string(video)}")
            
    
    def filter_string(self, video_info: str) -> str:
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
        return video_info.split()[2] + "  "+ video_info.split()[3]        
    
    
    def select_resolution_option(self):
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
        self.display_resolution_options()
        while True:
            try:
                resolution_option = int(input("Enter the number of the resolution you want: "))
                if resolution_option in range(1, len(self.get_videos_only()) + 1):
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
        resolution_option = self.select_resolution_option()
        video: str = videos[resolution_option - 1]
        resolution: str = video.split()[3].split('=')[1]
        YouTube(self.url).streams.get_by_resolution(resolution).download(output_path=self.download_path)
        print(f"Downloaded {self.url} to {self.download_path}")
        



if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=OpohbXB_JZU"