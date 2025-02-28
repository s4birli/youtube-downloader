#!/usr/bin/env python3
"""
YouTube Video Downloader
A script to download YouTube videos with quality selection options.
"""

import os
import sys
import logging
from typing import Dict, List, Optional, Any
import yt_dlp

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class VideoDownloader:
    """Handles YouTube video downloading operations."""
    
    def __init__(self) -> None:
        """Initialize the VideoDownloader with default configuration."""
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'progress_hooks': [self._progress_hook],
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True
        }

    @staticmethod
    def _progress_hook(d: Dict[str, Any]) -> None:
        """
        Handle download progress updates.
        
        Args:
            d: Dictionary containing download information
        """
        if d['status'] == 'downloading':
            sys.stdout.write(f"\rDownloading: {d.get('_percent_str', '0%')}")
            sys.stdout.flush()
        elif d['status'] == 'finished':
            print("\nDownload completed. Processing video...")

    @staticmethod
    def _clean_filename(title: str, max_length: int = 20) -> str:
        """
        Clean filename by removing invalid characters and limiting length.
        
        Args:
            title: Original filename
            max_length: Maximum length for the filename
            
        Returns:
            Cleaned filename
        """
        invalid_chars = '<>:"/\\|?*'
        clean_title = ''.join(char for char in title if char not in invalid_chars)
        return clean_title[:max_length].strip()

    def _get_video_formats(self, info: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Get available video formats sorted by quality.
        
        Args:
            info: Video information dictionary
            
        Returns:
            List of available video formats
        """
        formats = [f for f in info['formats'] 
                  if f.get('ext') == 'mp4' and f.get('filesize')]
        return sorted(formats, key=lambda x: x.get('filesize', 0), reverse=True)

    def _get_quality_choice(self, formats: List[Dict[str, Any]]) -> int:
        """
        Get user's quality choice.
        
        Args:
            formats: List of available formats
            
        Returns:
            Selected format index
        """
        while True:
            try:
                choice = input("\nSelect quality (1 for highest quality, or enter number): ").strip()
                if not choice:
                    return 0
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(formats):
                    return choice_idx
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def download_video(self) -> bool:
        """
        Handle the video download process.
        
        Returns:
            bool: False if user wants to exit, True otherwise
        """
        try:
            # Get video URL
            url = input("\nPlease enter the YouTube URL (or 'exit' to quit): ").strip()
            
            if url.lower() == 'exit':
                return False
                
            if not url.startswith(('http://www.youtube.com', 'https://www.youtube.com', 
                                 'http://youtu.be', 'https://youtu.be')):
                logger.error("Invalid YouTube URL. Please enter a valid URL.")
                return True

            logger.info("Fetching video information...")

            # Get video information
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(url, download=False)
                except yt_dlp.utils.DownloadError as e:
                    logger.error(f"Failed to fetch video info: {str(e)}")
                    return True

                logger.info(f"Title: {info['title']}")
                
                # Get available formats
                formats = self._get_video_formats(info)
                if not formats:
                    logger.error("No suitable video formats found.")
                    return True

                # Display available qualities
                print("\nAvailable qualities:")
                for i, f in enumerate(formats[:5], 1):
                    size_mb = f.get('filesize', 0) / (1024 * 1024)
                    print(f"{i}. {f.get('height', 'N/A')}p - {size_mb:.1f} MB")

                # Get user's quality choice
                choice_idx = self._get_quality_choice(formats[:5])
                
                # Update format based on user choice
                chosen_format = formats[choice_idx]
                self.ydl_opts['format'] = f"{chosen_format['format_id']}+bestaudio[ext=m4a]"
                
                # Download the video
                logger.info("Starting download...")
                ydl.download([url])
                logger.info("Download completed successfully!")

        except KeyboardInterrupt:
            logger.info("\nDownload cancelled by user.")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            
        return True 