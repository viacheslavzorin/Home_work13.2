from channel import Channel, PLVideo, Video, PlayList



# channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
# channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()

# print(vdud.title)
print(vdud.id)
print(vdud.title)
print(vdud.url)
print(vdud.description)
print(vdud.subscriberCount)
print(vdud.videoCount)
print(vdud.viewCount)
# vdud.channel_id ='aLdfZn13RXFrTrgUyaGb1A'#test
# print(vdud.channel_id)#test
# print(Channel.get_service)
print(vdud.get_service())
vdud.to_json()
if __name__ == '__main__':
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
ch2 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
print(ch2.title)
ch1 = Channel("UC1eFXmJNkjITxPFWTy6RsWg")

video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video1)
# Как устроена IT-столица мира / Russian Silicon Valley (English subs)
print(video2)
# Пушкин: наше все? (Литература)
# шаблон: 'название_видео (название_плейлиста)'
# print(video2.video_get())
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