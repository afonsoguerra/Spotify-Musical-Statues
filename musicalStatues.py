import keyboard
import time
import random

#Generally: Spotify play/pause is the space key. Get spotify in focus and run this in the background for random stop starts...

while True:
	timeDelay = 5+random.randrange(0, 20) #Generates delays between 5 and 25 seconds.
	print(timeDelay) #Just for some visual debugging so it prints something to the shell.
	time.sleep(timeDelay)
	keyboard.press_and_release('space') #Can be setup with other keys for other music players if needed.
