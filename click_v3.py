import pyautogui   #pip install pyautogui
import datetime
import sched, time
from random import randint

#define parameters below
duration = 8 #this is in hours

start_time = datetime.datetime.now()
stop_time = start_time + datetime.timedelta(hours = duration) #change this to minutes if need it for smaller time frame.
savedpos = pyautogui.position()

print start_time
print stop_time
#print savedpos

def move_down(): 
	pyautogui.moveTo(pyautogui.position()[0], pyautogui.position()[1]+10)
    #pyautogui.moveRel(0, 1)  # move mouse 1 pixel down

def move_up():
	pyautogui.moveTo(pyautogui.position()[0], pyautogui.position()[1]-10)
	#pyautogui.moveRel(0, -1) # move mouse 1 pixel up
	
def press_key():
	pyautogui.press('shift')
	
def check_for_movement():
		if pyautogui.position() == savedpos:
			print "position being changed automatically"
			#print pyautogui.position()
			#print savedpos
			#print datetime.datetime.now()
			move_down()
			move_up()
			press_key()
		else:
			print "position was changed manually"
			#print pyautogui.position()
			#print savedpos
			#print datetime.datetime.now()
	

while datetime.datetime.now() < stop_time:
	check_for_movement()
	savedpos = pyautogui.position()
	time.sleep(randint(60, 120))