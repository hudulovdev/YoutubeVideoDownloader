import pytube

def download_video(url):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully!")
    except pytube.exceptions.PytubeError as e:
        print(f"Error: {str(e)}")

# Example usage

video_url = input("Enter video link here: ")

download_video(video_url)
