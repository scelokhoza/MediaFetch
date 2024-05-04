from pytube import YouTube
import os



class DownloadAudio:
    def __init__(self, url):
        self.url = url
        self.download_path: str = os.path.join(os.path.expanduser('~'), 'Downloads')
        
    
    def get_audios_only(self) -> list:
        """
        This method fetches the audio streams from the YouTube URL.

        Args:
        self (DownloadAudio): An instance of the DownloadAudio class.

        Returns:
        list: A list of audio streams from the YouTube URL.

        Example:
        >>> download_audio_obj.get_audios_only()
        """
        yt = YouTube(self.url)
        audios: list = yt.streams.filter(mime_type="audio/mp4" ,adaptive=True).order_by('abr').desc()
        return audios
    
    
    def display_average_bitrate(self, audios: list) -> None:
        for i, audio in enumerate(audios):
            if self.is_downloadable(audio):
                print(f"{i+1}. {self.filter_string(audio)} DOWNLOAD")
            else:
                print(f"{i+1}. {self.filter_string(audio)} NOT AVAILABLE")
                
    
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
        stream = YouTube(self.url).streams.get_by_itag(stream_object.itag)
        if stream:
            return True
        return 
    
    
    def filter_string(self, audio_info: object) -> str:
        """
        This function filters the audio information string to extract the resolution details.

        Args:
        audio_info (str): The audio information string obtained from the YouTube object.

        Returns:
        str: A string containing the audio resolution in the format "widthxheight" and the audio format "audio/format".

        Example:
        >>> audio_info = "audio/mp4; abr=160kbps"
        >>> filter_string(audio_info)
        'audio/mp4' '160kbps'
        """
        return f"{audio_info.mime_type} {audio_info.abr}"
    
    
    def select_average_bitrate(self, audios: list):
        self.display_average_bitrate(audios)
        while True:
            try:
                resolution_option = int(input("Enter the number of the bitrate you want: "))
                if resolution_option in range(1, len(audios) + 1):
                    return resolution_option
                else:
                    print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")
                
    
    def download_audio(self):
        audios = self.get_audios_only
        resolution_option = self.select_average_bitrate(audios)
        audio = audios[resolution_option - 1]
        if self.is_downloadable(audio):
            YouTube(self.url).streams.get_by_resolution(resolution=audio.abr).download(output_path=self.download_path)
            print(f"Downloaded {self.url} to {self.download_path}")
        else:
            print(f"No stream available for {self.filter_string(audio)}")
            


if __name__ == "__main__":
    url: str = DownloadAudio()