# from threading import Timer
#
# timeout = 10
# t = Timer(timeout, print, ['Sorry, times up'])
# t.start()
# answer = input(f"You have {timeout} seconds to provide input")
# t.cancel()

import time
from threading import Thread
answer = None
def check():
    time.sleep(2)
    if answer != None:
        return
    print ("Too Slow")

Thread(target = check).start()

answer = input("Input something: ")