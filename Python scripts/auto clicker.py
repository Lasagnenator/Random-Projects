import ctypes
import time
import sys
from numba import jit,void,int32

@jit(cache=True)
def Click():
    ctypes.windll.user32.mouse_event(0x0002,0,0,0,0)
    ctypes.windll.user32.mouse_event(0x0004,0,0,0,0)

@jit(void(int32, int32), cache=True)
def activate_clicks(frequency, duration):
    #input("activate clicks")
    frequency = float(frequency)*2
    duration /= 2.0
    time_passed = 0
    while time_passed/frequency < duration:
        Click()
        time.sleep(1.0/frequency)
        time_passed += 1
    print("Clicks finished.")

@jit(void(int32), cache=True)
def getstate(key_code):
    return abs(ctypes.windll.user32.GetKeyState(key_code))>1

def main():
    print("Auto-clicker. Alt-C to activate.")
    print("Every computer has a different maximum hertz")
    print("Results varies if computer lags or limited cpu speed.")
    duration = int(input("Duration of clicks (seconds): "))
    frequency = int(input("Hertz of clicks: "))
    while True:
        if getstate(0x12) and getstate(0x43):
            activate_clicks(frequency, duration)
            #print("Alt+C")

if __name__ == "__main__":
    #input("breakpoint")
    main()

try:
    if __name__ == "__main__":
        input("breakpoint")
        main()
finally:
    print("Written by Matthew Richards")
    print("Ending")
    sys.exit()
