# YouTube Video Downloader

A simple yet powerful Python package to download YouTube videos in your preferred quality. This tool uses the `yt-dlp` library to provide reliable YouTube video downloads with quality selection options.

## Features

- Download YouTube videos in various qualities
- Show available video qualities with file sizes
- Interactive quality selection
- Progress bar during download
- Continuous download mode (download multiple videos)
- Clean filenames for downloaded videos
- Error handling for failed downloads
- Proper logging with timestamps

## Requirements

- Python 3.x
- yt-dlp library

## Project Structure

```
youtube_downloader/
├── youtube_downloader/
│   ├── __init__.py
│   ├── __main__.py
│   └── downloader.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/s4birli/youtubeDownloader
cd youtubeDownloader
```

2. Create and activate a virtual environment (recommended):
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
# If using virtual environment (recommended)
python -m youtube_downloader

# Or directly
python3 -m youtube_downloader
```

2. When prompted, paste the YouTube URL you want to download from.

3. The script will show available video qualities with their file sizes.

4. Select your preferred quality by entering the corresponding number (1-5).
   - 1 is typically the highest quality
   - Press Enter to select the highest quality automatically

5. The video will start downloading with a progress indicator.

6. After the download completes, you can:
   - Enter another URL to download more videos
   - Type 'exit' to quit the program

## Example

```
YouTube Video Downloader
==============================
Type 'exit' at any time to quit the program

Please enter the YouTube URL (or 'exit' to quit): https://youtube.com/watch?v=...
Fetching video information...
Title: Sample Video Title

Available qualities:
1. 1080p - 210.5 MB
2. 720p - 120.3 MB
3. 480p - 65.8 MB
4. 360p - 32.4 MB
5. 240p - 18.2 MB

Select quality (1 for highest quality, or enter number): 2
Downloading: 45.2%
```

## Features Explained

- **Quality Selection**: Choose from up to 5 different quality options for each video
- **File Size Information**: See the size of each quality option before downloading
- **Progress Tracking**: Real-time download progress indicator
- **Continuous Mode**: Download multiple videos without restarting the script
- **Error Handling**: Graceful handling of network issues and invalid URLs
- **Clean Filenames**: Automatically removes invalid characters from filenames
- **Logging**: Detailed logging with timestamps for better debugging

## Technical Details

The package uses:
- `yt-dlp`: A powerful library for downloading YouTube videos
- Python's built-in libraries for file handling and user interaction
- Type hints for better code maintenance
- Proper logging for debugging
- Object-oriented design for better code organization
- Error handling for robust operation
- Progress hooks for download status updates

## Development

To contribute to this project:

1. Fork the repository
2. Create a virtual environment
3. Install development dependencies:
```bash
pip install -r requirements.txt
```
4. Make your changes
5. Submit a pull request

## Limitations

- Only supports MP4 format
- Requires stable internet connection
- Subject to YouTube's terms of service
- Some videos might not be available for download due to restrictions

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's terms of service and copyright laws when downloading videos. 