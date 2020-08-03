from googleapiclient.discovery import build

from models import Channel


class YoutubeService:
    def __init__(self, token):
        self.youtube_build = build('youtube', 'v3', developerKey=token, cache_discovery=False)

    def get_popular_channels(self) -> dict:
        popular_channels_ids = list(map(lambda channel: channel.id, Channel.get_popular()))
        channels_data = self.youtube_build.channels().list(id=popular_channels_ids,
                                                           part="contentDetails").execute()
        result = dict()
        for channel in channels_data['items']:
            playlist_id = channel['contentDetails']['relatedPlaylists']['uploads']
            channel_videos = self.youtube_build.playlistItems().list(playlistId=playlist_id,
                                                                     part='snippet',
                                                                     maxResults=3).execute()
            for video in channel_videos['items']:
                result[video['snippet']['resourceId']['videoId']] = {
                    'title': video['snippet']['title'],
                    'picture': video['snippet']['thumbnails']['standard'],
                    'url': 'https://www.youtube.com/watch?v=%s' % video['snippet']['resourceId']['videoId']
                }

        return result
