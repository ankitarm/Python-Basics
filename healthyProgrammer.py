# # healthy programmer
#
from pygame import mixer
import datetime
import time

def musicfunction(file, stopper):
    mixer.music()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        i = input()
        if i == stopper:
            mixer.music.stop()

def logfunction(msg):
    with open("file","a") as f:
        f.write(msg+str(datetime.now()))


watertime=time.time()
eyestime=time.time()
exetime=time.time()

if time.time()-watertime>10:
    print("Time to drink water...Type drank to stop")
    musicfunction("song.mp3","drank")
    logfunction("he drank water at ")














# # Starting the mixer
# # mixer.init()
# # # Loading the song
# # mixer.music.load("song.mp3")
# # # Setting the volume
# # mixer.music.set_volume(0.7)
# # # Start playing the song
# # mixer.music.play()
# # time.sleep(15)
# # infinite loop
# # while True:
# #
# #     print("Press 'p' to pause, 'r' to resume")
# #     print("Press 'e' to exit the program")
# #     query = input(" ")
# #
# #     if query == 'p':
# #
# #         # Pausing the music
# #         mixer.music.pause()
# #     elif query == 'r':
# #
# #         # Resuming the music
# #         mixer.music.unpause()
# #     elif query == 'e':
# #
# #         # Stop the mixer
# #         mixer.music.stop()
# #         break
#
# from pygame import mixer
# import datetime
# import time
# a = datetime.datetime.now().hour
# print(a)
# # a = int(input("enter hr"))
#
# while a == 21:
#     while True:
#
#             print("water")
#             mixer.init()
#             mixer.music.load("song.mp3")
#             mixer.music.play()
#             query = input("Press 'done' to exit the program")
#             if query == "done":
#                 mixer.music.stop()
#                 with open("logfile.txt","a") as f:
#                     f.write(str(datetime.datetime.now())+" he drank water \n")
#             time.sleep(1200 - time.time() % 1200)
#     from pygame import mixer
#     import datetime
#     import time
#     while True:
#             print("water")
#             mixer.init()
#             mixer.music.load("song.mp3")
#             mixer.music.play()
#             query = input("Press 'done' to exit the program")
#             if query == "done":
#                 mixer.music.stop()
#                 with open("logfile.txt","a") as f:
#                     f.write(str(datetime.datetime.now())+" he drank water \n")
#             time.sleep(1800 - time.time() % 1800)
#     from pygame import mixer
#     import datetime
#     import time
#     while True:
#             print("water")
#             mixer.init()
#             mixer.music.load("song.mp3")
#             mixer.music.play()
#             query = input("Press 'done' to exit the program")
#             if query == "done":
#                 mixer.music.stop()
#                 with open("logfile.txt","a") as f:
#                     f.write(str(datetime.datetime.now())+" he drank water \n")
#             time.sleep(1200 - time.time() % 1200)
