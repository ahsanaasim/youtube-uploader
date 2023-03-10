![YouTube Upload Logo](youtube.png)


[![MIT 
licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# YouTube Uploader

**This is a boilerplate Python project to upload videos in YouTube**

### To initialize

    uploader = YTUploader()

### To upload a video

    video = uploader.upload('ayah__CLIP.mp4', tags=["quran", "islam", "surah", "ayah"])

### To add a video in a playlist
    
    uploader.addToPlaylist('PL23CtYg4XgaYMOTqjuq1oOktjUkDNUGZP', 'gZDArq_C4kc')

### To add a playlist
    
    uploader.createPlaylist('Python Playlist', 'Python description', 'private')

### Important
Need to modify the YOUTUBE_UPLOAD_SCOPE in __init__.py file inside the youtube-upload package with the following scopes

    YOUTUBE_UPLOAD_SCOPE = [
        "https://www.googleapis.com/auth/youtube",
        "https://www.googleapis.com/auth/youtube.force-ssl",
        "https://www.googleapis.com/auth/youtube.upload"
    ]

# License
[The MIT License (MIT)](LICENSE)

