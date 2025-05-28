import yt_dlp
import os

def download_youtube_mp4(url, resolution='720'):
    
    format_str = f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]'

    # Create output directory if it doesn't exist
    output_dir = r'Your Directory'
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
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("Enter the YouTube link you want to download: ")
    quality = input("Send desired resolution (720, 1080, 1440): ")
    if quality not in ['720', '1080', '1440']:
        print("Resolution not supported. Select 720, 1080 or 1440 only.")
    else:
        download_youtube_mp4(video_url, quality)
