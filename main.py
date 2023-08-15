from pytube import YouTube
from moviepy.editor import VideoFileClip

# 다운로드할 동영상 URL 리스트
links = ['link']

# 동영상 다운로드 함수
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

# 동영상 다운로드 및 mp3로 변환하는 함수
def download_and_convert_to_mp3(links):
    for link in links:
        try:
            yt = YouTube(link)
            stream = yt.streams.filter(only_audio=True).first()
            print(f"Downloading {yt.title}...")
            file_path = stream.download()
            print("Download completed.")

            mp3_file_path = file_path.split(".")[0] + ".mp3"
            with VideoFileClip(file_path) as video:
                audio = video.audio
                print(f"Converting {yt.title} to mp3...")
                audio.write_audiofile(mp3_file_path)
                audio.close()
                video.close()

            print(f"Conversion of {yt.title} to mp3 completed.")
        except Exception as e:
            print(f"Unable to download and convert video from {link}. Error: {e}")

# 동영상 다운로드 함수 실행
download_videos(links)

# 동영상 다운로드 및 mp3 변환 함수 실행
download_and_convert_to_mp3(links)
