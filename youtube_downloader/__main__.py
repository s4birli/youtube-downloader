#!/usr/bin/env python3
"""Main entry point for the YouTube Video Downloader."""

import sys
import logging
from .downloader import VideoDownloader

logger = logging.getLogger(__name__)

def main() -> None:
    """Main entry point of the script."""
    try:
        print("YouTube Video Downloader")
        print("=" * 30)
        print("Type 'exit' at any time to quit the program")
        
        downloader = VideoDownloader()
        while True:
            print("\n" + "=" * 30)
            if not downloader.download_video():
                print("\nThank you for using YouTube Video Downloader!")
                break
                
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 