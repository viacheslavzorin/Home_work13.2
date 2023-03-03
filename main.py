from channel import Channel
#import json
# channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'

vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
#print(vdud.title)
print(vdud.id)
print(vdud.title)
print(vdud.url)
print(vdud.description)
print(vdud.subscriberCount)
print(vdud.videoCount)
print(vdud.viewCount)
vdud.channel_id = 'Новое название'
print(vdud.channel_id)
#print(Channel.get_service)
print(vdud.get_service())
vdud.to_json()