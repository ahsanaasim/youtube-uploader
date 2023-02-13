from youtube_upload.client import YoutubeUploader
import shutil

class YTUploader:
    def __init__(self):
        self.uploader = YoutubeUploader()
        shutil.copy('google-oauth.json', 'oauth.json')
        self.uploader.authenticate(oauth_path='oauth.json')
        shutil.copy('oauth.json', 'google-oauth.json')

    def upload(self, path, tags = []):
        options = {
            "title" : "Example title", # The video title
            "description" : "Example description", # The video description
            "tags" : tags,
            "categoryId" : "22",
            "privacyStatus" : "public", # Video privacy. Can either be "public", "private", or "unlisted"
            "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
            # "thumbnailLink" : "https://cdn.havecamerawilltravel.com/photographer/files/2020/01/youtube-logo-new-1068x510.jpg" # Optional. Specifies video thumbnail.
        }

        # upload video
        # self.uploader.upload(path, options) 