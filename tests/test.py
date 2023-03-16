from channel import Channel, Video, PLVideo, PlayList, isodate, datetime
import pytest


def test_str():
    ch3 = Channel("UC1eFXmJNkjITxPFWTy6RsWg")
    assert ch3.__str__() == "Yotube-канал: Редакция"


def test_add():
    ch4 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch5 = Channel("UC1eFXmJNkjITxPFWTy6RsWg")
    assert ch4.__add__(ch5) == '103000003700000'


def test_lt():
    ch4 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch5 = Channel("UC1eFXmJNkjITxPFWTy6RsWg")
    assert ch4.__lt__(ch5) == False
    assert ch5.__lt__(ch4) == True


def test_video_init():
    video1 = Video('BBotskuyw_M')
    assert video1.video_titl == "Пушкин: наше все?"


def test_video_str():
    video1 = Video('BBotskuyw_M')
    assert video1.__str__() == "Пушкин: наше все?"


def test_plvideo_init():
    plvideo1 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert plvideo1.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'


def test_plvideo_str():
    plvideo1 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert plvideo1.__str__() == "Пушкин: наше все? Литература"


def test_playlist_init():
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    assert pl.playl_name == "Редакция. АнтиТревел"


def test_total_duration():
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    assert pl.total_duration == datetime.timedelta(seconds=13261)


def test_best_video():
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    assert pl.best_video() == "https:/www.youtube.com/wath?v=9Bv2zltQKQA"
