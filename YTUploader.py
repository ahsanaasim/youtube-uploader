from youtube_upload.client import YoutubeUploader
import shutil

class YTUploader:
    def __init__(self):
        self.uploader = YoutubeUploader()
        shutil.copy('google-oauth.json', 'oauth.json')
        self.uploader.authenticate(oauth_path='oauth.json')
        shutil.copy('oauth.json', 'google-oauth.json')

    def upload(self, path, title="", description="", categoryId="", privacyStatus="private", kids=False, tags = [], thumbnailLink=""):
        options = {
            "title" : title, # The video title
            "description" : description, # The video description
            "tags" : tags,
            "categoryId" : categoryId,
            "privacyStatus" : privacyStatus, # Video privacy. Can either be "public", "private", or "unlisted"
            "kids" : kids, # Specifies if the Video if for kids or not. Defaults to False.
            "thumbnailLink" : thumbnailLink # Optional. Specifies video thumbnail.
        }

        # upload video
        self.uploader.upload(path, options) 