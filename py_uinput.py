import uinput
import time

def mouse_move():
    
    time.sleep(1)
    with uinput.Device([uinput.REL_X, uinput.REL_Y]) as mdevice:
        time.sleep(1)
        for i in range(20):
            mdevice.emit(uinput.REL_X, 5);
            mdevice.emit(uinput.REL_Y, 5);

def key_clicks():
    
    with uinput.Device([uinput.KEY_A,
                        uinput.KEY_1,
                        uinput.KEY_Q,
                        uinput.KEY_E,
                        uinput.KEY_H,
                        uinput.KEY_L,
                        uinput.KEY_O]) as device:
        time.sleep(1)
        device.emit_click(uinput.KEY_H)
        device.emit_click(uinput.KEY_E)
        device.emit_click(uinput.KEY_L)
        device.emit_click(uinput.KEY_L)
        device.emit_click(uinput.KEY_O)

        
        
def print_keys():
    print("REL_X: " + str(uinput.REL_X))
    print("REL_Y: " + str(uinput.REL_Y))
    print("KEY_A: " + str(uinput.KEY_A))
    print("KEY_Q: " + str(uinput.KEY_Q))
    print("KEY_1: " + str(uinput.KEY_1))
    print("KEY_E: " + str(uinput.KEY_E))
    print("KEY_H: " + str(uinput.KEY_H))
    print("KEY_L: " + str(uinput.KEY_L))
    print("KEY_O: " + str(uinput.KEY_O))
        
def main():
    print_keys()
    key_clicks()
    mouse_move()
        
        
        
 

if __name__ == "__main__":
    main()
    
