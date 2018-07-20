# Lirc control file for 44 key led remote
# Commands are taken from the corresponding lirc config file
# and execute in a terminal enviroment 
import subprocess

def lightup():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_BRIGHTNESSUP"])

def lightdown():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_BRIGHTNESSDOWN"])

def pause():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_PAUSE"])

def on():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_POWER"])

def red():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_0"])

def green():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_1"])

def blue():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_2"])

def white():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_3"])

def orange():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_4"])

def lightgreen():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_5"])

def deepblue():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_6"])

def milkwhite():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_7"])

def deepyellow():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_8"])

def cyan():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_9"])

def bluepurple():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_AB"])

def pinkwhite():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_AGAIN"])

def yellow():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_AUDIO"])

def lightblue():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_AUX"])

def purple():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_B"])

def greenwhite():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_BACK"])

def lightyellow():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_BLUE"])

def skyblue():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_BREAK"])

def brown():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_C"])

def bluewhite():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_CALC"])

def increasered():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_CD"])

def increasegreen():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F"])

def increaseblue():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F1"])

def faster():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F10"])

def reducered():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F11"])

def reducegreen():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F12"])

def reduceblue():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F13"])

def slower():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F14"])

def diy1():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F15"])

def diy2():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F16"])

def diy3():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_17"])

def auto():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F18"])

def diy4():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F19"])

def diy5():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F2"])

def diy6():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F20"])

def flash():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F21"])

def jump3():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F22"])

def jump7():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F23"])

def fade3():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F24"])

def fade7():
    rtn = subprocess.call(["irsend", "SEND_ONCE", "44led", "KEY_F3"])
