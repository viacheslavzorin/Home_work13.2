import json
import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('MY_API_KEY')
# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


# channel_id = 'aLdfZn13RXFrTrgUyaGb1A'    # Редакция

class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
