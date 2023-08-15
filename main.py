from pytube import YouTube


links = ['https://www.youtube.com/shorts/lXzsHev559Y']


def download_videos(links):
    for link in links:
        try:
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            print(f"Downloading {yt.title}...")
            stream.download()
            print("Download completed.")
        except Exception as e:
            print(f"Unable to download video from {link}. Error: {e}")

download_videos(links)