import pygame as pg
import time
import mutagen.mp3
import datetime


var_time_to_drink = time.time()
var_time_to_ex =  time.time()
var_time_to_eye = time.time()

drink_interval = 1200 #Seconds_to_drink_water_that_are_20mins
ex_interval = 1800
eye_intervel = 2000

def glass_calculator(liter_to_Drink):
    size_of_glass_ml = 125
    liter_is_equal_to_ml = liter_to_Drink*1000
    number_of_glass = liter_is_equal_to_ml//size_of_glass_ml
    return  number_of_glass

def Mp3Length_finder(_file_to_len):
    audio_file = mutagen.mp3.MP3(_file_to_len)
    length_of_file = audio_file.info.length
    return length_of_file
#
def func_playsound(file):
    pg.mixer.init()
    pg.mixer.music.load(file)
    pg.mixer.music.play()
    time.sleep(Mp3Length_finder(file)) #To_play_complete_sound

tota_glass = glass_calculator(1)

while True:
    if time.time()- var_time_to_drink > drink_interval and tota_glass >0:
         while True:
             func_playsound("sample.mp3")
             if input("type done after drinking water").lower() == "done":
                 var_time_to_drink = time.time()
                 File = open("LogFile",'a')
                 File.write(f"[{datetime.datetime.now()}] Drank water\n")
                 tota_glass= tota_glass-1
                 print(tota_glass)
                 break
    if time.time()-var_time_to_ex > ex_interval:
         while True:
             if input("Type done after exercise").lower() == "done":
                  var_time_to_ex = time.time()
                  File = open("LogFile", 'a')
                  File.write(f"[{datetime.datetime.now()}] Drank water\n")
                  break
    if time.time()-var_time_to_eye > eye_intervel:
        while True:
              if input("Type done after Eyes relaxation").lower() == "done":
                var_time_to_eye = time.time()
                File = open("LogFile", 'a')
                File.write(f"[{datetime.datetime.now()}] Drank water\n")
    time.sleep(20)



