from pytube import YouTube
import os


# YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.get_by_resolution('7').



class DownloadVideo:
    def __init__(self, url)-> None:
        self.url = url
        self.download_path: str = os.path.join(os.path.expanduser('~'), 'Downloads')
        
    
    def get_videos_only(self) -> list:
        try:
            yt = YouTube(self.url)
            videos: list = yt.streams.filter(mime_type="video/mp4" ,progressive=True)
            return videos
        except ConnectionError:
            print("Connection Error, check your internet connection!!")
            return []
    
    
    def display_resolution_options(self):
        videos: list = self.get_videos_only()
        for i, video in enumerate(videos):
            print(f"{i+1}. {self.filter_string(video)}")
            
    
    def filter_string(self, video_info: str) -> str:
        return video_info.split()[2] + "  "+ video_info.split()[3]        
    
    
    def select_resolution_option(self):
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
        videos = self.get_videos_only()
        resolution_option = self.select_resolution_option()
        video: str = videos[resolution_option - 1]
        resolution: str = video.split()[3].split('=')[1]
        YouTube(self.url).streams.get_by_resolution(resolution).download(output_path=self.download_path)
        print(f"Downloaded {self.url} to {self.download_path}")
        



if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=OpohbXB_JZU"