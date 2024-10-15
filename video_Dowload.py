import yt_dlp

# Copy the url of your video here!!!
url = "https://www.youtube.com/watch?v=WTLmfdFyvcs"

ydl_opts = {
    'format': 'best',  # To get the best video quality
    'outtmpl': '%(title)s.%(ext)s',  # Output filename template
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=True)
    video_title = info_dict.get('title', None)
    print(f"Downloaded: {video_title}")
