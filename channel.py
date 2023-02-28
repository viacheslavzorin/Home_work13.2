import json
import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('MY_API_KEY')
# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


# channel_id = 'aLdfZn13RXFrTrgUyaGb1A'    # Редакция

#class Channel:
    #channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    #def __init__(self, channel_id):
        #self.__channel_id = channel_id

class Channel:
    def __init__(self, channel_id):
        self.__channel_id = channel_id

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        if channel_id:
            print ('UserWarning запрещено')
        else:
            self.__x = channel_id

    def print_info(self):
        #channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel = self.channel_get()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def channel_get(self):
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    @property
    def title(self):
        return self.channel_get()['items'][0]['snippet']['title']
    @title.setter
    def title(self,name):
        name = self.channel_get()

    @property
    def id(self):
        return self.channel_get()['items'][0]['id']

    #@id.setter
    #def title(self, data):
        #data = self.channel_get()
    @property
    def url(self):
        return self.channel_get()['items'][0]['snippet']['thumbnails']['default']['url']

    @property
    def subscriberCount(self):
        return self.channel_get()['items'][0]['statistics']['subscriberCount']

    @property
    def videoCount(self):
        return self.channel_get()['items'][0]['statistics']['videoCount']

    @property
    def viewCount(self):
        return self.channel_get()['items'][0]['statistics']['viewCount']

    @property
    def description(self):
        return self.channel_get()['items'][0]['snippet']['description']
    #@property
    def get_service(self):
        return  build('youtube', 'v3', developerKey=api_key)

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

#data = {"ttt": 1}
#with open("filename.json", "w", encoding="UTF-8") as file:
    #json.dump(data, file, indent=2, ensure_ascii=False)


#print(Channel.get_service)
#channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
#channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
#x = json.dumps(channel, indent=2, ensure_ascii=False)
#print(type(channel['items']))
#print(channel['items'])
#print(channel['items'].pop(0))
#print(channel['items'].pop(0)['snippet']['thumbnails']['default']['url'])
#print(channel['items'].pop(0)['id'])
#print(channel['items'][0]['snippet']['title'])
#print(channel['items'][0]['snippet']['description'])
#print(channel['items'][0]['statistics']['viewCount']) #Количество просмотров
#print(channel['items'][0]['statistics']['videoCount'])
#print(channel['items'].pop(0)['statistics']['subscriberCount'])
#print(channel['items'][0])
#print(channel['items'][0]['snippet']['thumbnails']['default']['url'])
#print(channel['items'][0]['statistics']['subscriberCount'])
#print(len(channel))
