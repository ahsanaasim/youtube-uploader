from YTUploader import YTUploader
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

uploader = YTUploader()
# video = uploader.upload('ayah__CLIP.mp4', tags=["quran", "islam", "surah", "ayah"])

def main():
    print("main function")
    # uploader.createPlaylist('Python Playlist', 'Python description', 'private')
    # uploader.addToPlaylist('PL23CtYg4XgaYMOTqjuq1oOktjUkDNUGZP', 'gZDArq_C4kc')


main()