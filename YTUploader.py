from youtube_upload.client import YoutubeUploader
import shutil
import json

import google.oauth2.credentials
import googleapiclient.discovery
import googleapiclient.errors

class YTUploader:
    def __init__(self):
        self.uploader = YoutubeUploader()
        # self.uploader.authenticate()
        shutil.copy('google-oauth.json', 'oauth.json')
        self.uploader.authenticate(oauth_path='oauth.json')
        shutil.copy('oauth.json', 'google-oauth.json')

    def makeCredentials(self):
        c = {}
        with open('google-oauth.json', 'r') as f:
            c = json.load(f)
        return google.oauth2.credentials.Credentials(
            c["access_token"],
            refresh_token = c["refresh_token"],
            token_uri = c["token_uri"],
            client_id = c["client_id"],
            client_secret = c["client_secret"],
            scopes = c["scopes"]
        )
    
    def generateBuilder(self):
        api_service_name = "youtube"
        api_version = "v3"
        self.builder = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=self.makeCredentials())

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
        return self.uploader.upload(path, options) 

    def createPlaylist(self, title, description, privacyStatus='public'):
        request_body = {
                'snippet': {
                    'title': title,
                    'description': description,
                },
                'status': {
                    'privacyStatus': privacyStatus
                }
            }
        request = self.builder.playlists().insert(
            part='snippet,status',
            body=request_body
        )
        response = request.execute()
        print('response[id]', response['id'])
        print('response[title]', response['snippet']['title'])
        return response

    def addToPlaylist(self, playlistId, videoId):
        request_body = {
                'snippet': {
                    'playlistId': playlistId,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': videoId
                    }
                }
            }
        request = self.builder.playlistItems().insert(
            part='snippet',
            body=request_body
        )
        response = request.execute()
        return response
        