import os, sys
from pynput.mouse import Listener
num = 1
def take_screnshot(dirname):
	def on_click(x, y, button, pressed):
		global num
		btn = button.name
		if button.name == "left":
			if pressed:
				filename = f"{dirname}{num}"
				os.system(f"scrot -u -p ./{dirname}/{filename}.png")
				num+=1
				print(num)
	    
	
	with Listener(on_click=on_click) as listener:
	    listener.join()


cmd = input("Commands :- 1)RECORD:- ")
if cmd == "1":
	name_of_steps = input("in what name do you want to save screenshots:- ")
	os.system(f"mkdir {name_of_steps}")
	print("click after every step an screenshot will be taken")
	print("To stop ctrl-c the script currently i am working on a better way of doing it but for now this the best")
	take_screnshot(name_of_steps)







