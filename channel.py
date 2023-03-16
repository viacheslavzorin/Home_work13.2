import datetime
import json, isodate
import os
import isodate
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('MY_API_KEY')
# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


# UC1eFXmJNkjITxPFWTy6RsWg редакия
# channel_id = 'aLdfZn13RXFrTrgUyaGb1A'    # Редакция
class Channel:
    def __init__(self, channel_id):
        self.__channel_id = channel_id

        self.id = self.channel_get()['items'][0]['id']
        self.url = self.channel_get()['items'][0]['snippet']['thumbnails']['default']['url']
        self.title = self.channel_get()['items'][0]['snippet']['title']
        self.subscriberCount = self.channel_get()['items'][0]['statistics']['subscriberCount']
        self.videoCount = self.channel_get()['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel_get()['items'][0]['statistics']['viewCount']
        self.description = self.channel_get()['items'][0]['snippet']['description']

    def print_info(self):
        # channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel = self.channel_get()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def channel_get(self):
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    # @property
    # def channel_id(self):
    # return self.__channel_id

    # @channel_id.setter
    # def channel_id(self, channel_id):
    # if channel_id:
    # print('UserWarning запрещено')
    # else:
    # self.__x = channel_id

    def get_service(self):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self):
        data = {
            "title": self.title,
            "id": self.id,
            "url": self.url,
            "subscriberCount": self.subscriberCount,
            "videoCount": self.videoCount,
            " viewCount": self.viewCount,
            "description": self.description
        }
        with open("filename.json", "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        return f"Yotube-канал: {self.title}"

    def __add__(self, other):
        """сложение"""
        return self.subscriberCount + other.subscriberCount

    def __lt__(self, other):
        """Сравнение"""
        return self.subscriberCount > other.subscriberCount


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_titl = self.video_get()['items'][0]['snippet']['title']
        self.video_viewCount = self.video_get()['items'][0]['statistics']['viewCount']
        self.video_likeCount = self.video_get()['items'][0]['statistics']['likeCount']

    def video_get(self):
        video_response = youtube.videos().list(part='snippet,statistics',
                                               id=self.video_id
                                               ).execute()
        return video_response

    def __str__(self):
        return f"{self.video_titl}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_name = self.playlist['items'][0]['snippet']['title']

    def __str__(self):
        return f"{self.video_titl} {self.playlist_name}"


class PlayList:
    """Вывод статистики плайлиста"""

    def __init__(self, id_playl):
        self.id_playl = id_playl
        super().__init__()
        self.playl = youtube.playlists().list(id=self.id_playl, part='snippet, contentDetails',
                                              maxResults=50).execute()
        self.url_playl = f"https://www.youtube.com/playlist?list={self.id_playl}"
        self.playl_name = self.playl['items'][0]['snippet']['title']
        self.playl_videos = youtube.playlistItems().list(playlistId=id_playl,
                                                         part='contentDetails',
                                                         maxResults=50,
                                                         ).execute()

        """ получить все id видеороликов из плейлиста"""
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playl_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.video_ids)
                                                    ).execute()

    """Длительность видео в плейлисте"""

    @property
    def total_duration(self):
        duration = datetime.timedelta(0)
        for video in self.video_response['items']:
            # Длительности YouTube-видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def best_video(self):

        b = 0
        for i in pl.video_ids:
            a = Video(i)
            # print(a.video_likeCount)
            c = int(a.video_likeCount)
            if c > b:
                b = c
                d = i
        return f"https:/www.youtube.com/wath?v={d}"


# class PlayList(MixPlayList):
# pass
s = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(s.playlist_name)
print(s.playlist)
d = PlayList('PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(d.playl)
print(d.playl_name)

pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.playl_name)
print(pl.playl_videos)
print(pl.video_ids)
duration = pl.total_duration
print(duration)

print(pl.best_video())
