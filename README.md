# YouTube Video Downloader

A simple Python script to download YouTube videos in different resolutions (720p, 1080p, or 1440p).

## Features

- Download YouTube videos in MP4 format
- Choose video resolution (720p, 1080p, or 1440p)
- Automatic video and audio merging
- Progress display during download
- Downloads are saved to a specified directory

## Requirements

- Python 3.x
- yt-dlp library

## Installation

1. Clone this repository or download the script
2. Install the required package:
```bash
pip install yt-dlp
```

## Usage

1. Run the script:
```bash
python convert.py
```

2. When prompted:
   - Enter the YouTube video URL
   - Choose the desired resolution (720, 1080, or 1440)

The downloaded video will be saved in the `C:\Users\ASUS\Pictures\video` directory with the video's title as the filename.

## Notes

- The script only supports single video downloads (no playlists)
- Supported resolutions are 720p, 1080p, and 1440p
- Videos are automatically merged into MP4 format
- The script will create the output directory if it doesn't exist

## License

This project is open source and available under the MIT License. 