import yt_dlp
import os
import re

def is_valid_youtube_url(url):
    # Regular expression pattern for YouTube URLs
    youtube_regex = r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'
    return bool(re.match(youtube_regex, url))

def download_youtube_mp4(url, resolution='720'):
    # Validate URL first
    if not is_valid_youtube_url(url):
        raise ValueError("Invalid YouTube URL. Please enter a valid YouTube video link.")
    
    # Modified format string to ensure audio is included
    format_str = f'bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/best[height<={resolution}]'

    # Create output directory if it doesn't exist
    output_dir = r'C:\Users\ASUS\Pictures\video'
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': format_str,
        # create new namefile in the specified directory
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),

        # merge video and audio files into mp4.
        'merge_output_format': 'mp4',

        # show progress
        'quiet': False,

        # don't download playlist
        'noplaylist': True,

        # Ensure audio is downloaded
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    while True:
        video_url = input("Enter the YouTube link you want to download: ")
        if is_valid_youtube_url(video_url):
            break
        print("Invalid YouTube URL. Please enter a valid YouTube video link.")
    
    print("\nSelect video quality:")
    print("1. 720p")
    print("2. 1080p")
    
    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "1":
        quality = "720"
    elif choice == "2":
        quality = "1080"
    else:
        print("Invalid choice. Defaulting to 720p.")
        quality = "720"
    
    download_youtube_mp4(video_url, quality)
