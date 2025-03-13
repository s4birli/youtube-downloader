# YouTube Video Downloader

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![YouTube](https://img.shields.io/badge/YouTube-Download-red.svg)](https://github.com/s4birli/youtube-downloader)

A powerful and user-friendly Python tool for downloading YouTube videos in your preferred quality. Built with `yt-dlp`, this tool offers an interactive command-line interface to download videos with quality selection, progress tracking, and proper error handling.

## 🚀 Key Features

- 📥 Download YouTube videos in various qualities (up to 1080p)
- 📊 Show available video qualities with file sizes
- 🎯 Interactive quality selection
- 📈 Real-time progress bar during download
- 🔄 Continuous mode for multiple video downloads
- 🧹 Clean filenames for downloaded videos
- ⚠️ Comprehensive error handling
- 📝 Detailed logging with timestamps

[View Demo](#example) | [Installation](#installation) | [Usage](#usage) | [Contributing](#contributing)

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

- Python 3.x (Not compatible with Python 2.x)
- yt-dlp library

## Project Structure

```
youtube_downloader/
├── youtube_downloader/
│   ├── __init__.py      # Package initialization
│   ├── __main__.py      # Entry point
│   └── downloader.py    # Main functionality
├── requirements.txt      # Project dependencies
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
└── LICENSE             # MIT License
```

## Installation

1. Make sure you have Python 3.x installed:
```bash
python3 --version
```
If not installed, you can install it:
- On macOS (using Homebrew):
  ```bash
  brew install python3
  ```
- On Ubuntu/Debian:
  ```bash
  sudo apt-get update
  sudo apt-get install python3
  ```

2. Clone this repository:
```bash
git clone https://github.com/s4birli/youtube-downloader
cd youtube-downloader
```

3. Create and activate a virtual environment (recommended):
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
# Make sure your virtual environment is activated
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Run the package
python -m youtube_downloader
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
2. Clone your fork:
```bash
git https://github.com/s4birli/youtube-downloader
cd youtube-downloader
```

3. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```