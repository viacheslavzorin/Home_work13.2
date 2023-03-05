from channel import Channel
import pytest

def test_str():
    ch3 = Channel("UC1eFXmJNkjITxPFWTy6RsWg")
    assert ch3.__str__() == "Yotube-канал: Редакция"

def test_add():
    ch4 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA' )
    ch5 = Channel("UC1eFXmJNkjITxPFWTy6RsWg" )
    assert ch4.__add__(ch5) == '103000003700000'

def test_lt():
    ch4 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch5 = Channel("UC1eFXmJNkjITxPFWTy6RsWg")
    assert ch4.__lt__(ch5) == False
    assert ch5.__lt__(ch4) == True