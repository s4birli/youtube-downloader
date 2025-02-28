import yt_dlp
import os

def clean_filename(title):
    # Remove invalid characters from filename and limit to 20 characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    return title[:20].strip()

def download_video():
    try:
        # Get the YouTube URL from user
        url = input("Please enter the YouTube URL (or 'exit' to quit): ").strip()
        
        if url.lower() == 'exit':
            return False
            
        print("Fetching video information...")

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'progress_hooks': [lambda d: print(f"\rDownloading: {d['_percent_str']}", end="")],
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True
        }

        # Create yt-dlp object and get video info
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info
            info = ydl.extract_info(url, download=False)
            
            # Show video title
            print(f"Title: {info['title']}")
            
            # Show available formats
            formats = [f for f in info['formats'] if f.get('ext') == 'mp4' and f.get('filesize')]
            formats.sort(key=lambda x: x.get('filesize', 0), reverse=True)
            
            print("\nAvailable qualities:")
            for i, f in enumerate(formats[:5], 1):  # Show top 5 qualities
                size_mb = f.get('filesize', 0) / (1024 * 1024)
                print(f"{i}. {f.get('height', 'N/A')}p - {size_mb:.1f} MB")
            
            # Let user choose quality
            while True:
                try:
                    choice = input("\nSelect quality (1 for highest quality, or enter number): ")
                    if not choice.strip():
                        choice = "1"
                    choice = int(choice)
                    if 1 <= choice <= len(formats[:5]):
                        break
                    print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Update format based on user choice
            chosen_format = formats[choice - 1]
            ydl_opts['format'] = f"{chosen_format['format_id']}+bestaudio[ext=m4a]"
            
            # Download the video
            print("\nDownloading video...")
            ydl.download([url])
            
            print(f"\nDownload completed successfully!")
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    
    return True

def main():
    print("YouTube Video Downloader")
    print("=" * 30)
    print("Type 'exit' at any time to quit the program")
    
    while True:
        print("\n" + "=" * 30)
        if not download_video():
            print("\nThank you for using YouTube Video Downloader!")
            break

if __name__ == "__main__":
    main() 