import json
import os

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

    #@property
    #def channel_id(self):

        #return self.__channel_id




    #@channel_id.setter
    #def channel_id(self, channel_id):
         #if channel_id:
              #print('UserWarning запрещено')
         #else:
              #self.__x = channel_id

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
        return self.subscriberCount + other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount > other.subscriberCount

    #def __lt__(self, other):
        #return self.subscriberCount < other.subscriberCount
