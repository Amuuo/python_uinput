import uinput
import time

def mouse_move():
    
	time.sleep(1)
	with uinput.Device([uinput.REL_X, uinput.REL_Y]) as mdevice:
		time.sleep(1)
		for i in range(40):
			time.sleep(0.01)
			mdevice.emit(uinput.REL_X, 5)
			mdevice.emit(uinput.REL_Y, 5)
def main():
	mouse_move()
        
 

if __name__ == "__main__":
	main()
