import pygame as pg
import time
import mutagen.mp3
import datetime

def time_to_Drink():
    time_now = datetime.datetime.now()
    time_after_30min = time_now + datetime.timedelta(minutes=30)
    print(time_now)
    print(time_after_30min)

def Mp3Length_finder(_file_to_len):
    audio_file = mutagen.mp3.MP3(_file_to_len)
    length_of_file = audio_file.info.length
    return length_of_file
#
def func_playsound(file):
    pg.mixer.init()
    pg.mixer.music.load(file)
    pg.mixer.music.play()
    time.sleep(Mp3Length_finder(file))
    pg.mixer.unload()

print(time_to_Drink())


