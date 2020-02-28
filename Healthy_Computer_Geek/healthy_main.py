import pygame as pg
import time
import mutagen.mp3
import datetime
from threading import Thread

def time_to_Drink():
    unformated_time = datetime.datetime.now()
    current_time = unformated_time.strftime("%H:%M:%S")
    time_after_30min = current_time + datetime.timedelta(minutes=30)
    print(current_time)
    print(time_after_30min)

var_time_to_drink = time.time()
var_time_to_ex =  time.time()
var_time_to_eye = time.time()

drink_interval = 1200 #Seconds_to_drink_water_that_are_20mins
ex_interval = 1800
eye_intervel = 2000


def Mp3Length_finder(_file_to_len):
    audio_file = mutagen.mp3.MP3(_file_to_len)
    length_of_file = audio_file.info.length
    return length_of_file
#
def func_playsound(file):
    pg.mixer.init()
    pg.mixer.music.load(file)
    pg.mixer.music.play()
    #time.sleep(Mp3Length_finder(file))


#time.time() - var_time_to_drink > drink_interval
if time.time()- var_time_to_drink > drink_interval :
    while True:
        func_playsound("sample.mp3")
        if input("type done after drinking water").lower() == "done":
            var_time_to_drink = time.time()
            break

if time.time()-var_time_to_ex > ex_interval:
    while True:
        if input("Type done after exercise").lower() == "done":
            var_time_to_ex = time.time()
            break

if time.time()-var_time_to_eye > eye_intervel:
    while True:
        if input("Type done after Eyes relaxation").lower() == "done":
            var_time_to_eye = time.time()
            break



