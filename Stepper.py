#  Stepping motor control program
#  a time (t) of .05 seconds takes 20 seconds per revolution
#  So, 0.1 second pulses (Only the up pulse rotates the shaft), must be 200 poles!
#  Now can control using a pot! For exact timing is better to write it in for "t"

import machine
import utime
 
step = machine.Pin(10, machine.Pin.OUT)
direction = machine.Pin(11, machine.Pin.OUT)
analog_value = machine.ADC(28)
seconds = 0

           #  t = .15 #  0.15 will rotate in exactly 1 minute                  
d = 0      # high = CCW, low = CW

while True:
    reading = analog_value.read_u16()  # Full CCW of pot, value 2, at CW, is about .007  Pot gives 256 to 65535 out
    t = (256*2)/reading   #  At .007 seconds the stepper motor gets confused.  max rotation = 2.78 seconds
    tt=(t)   #  Use "t" for variable speed, ".15" for 1 minute, .15/2 for 30 sec rotation etc
    seconds = t * 60 /0.15    #.15 = 1 minute = 60 seconds
    step.value(1)
    direction.value(d)
    utime.sleep(tt)   
    step.value(0)
    utime.sleep(tt)
    #      print (seconds)
    #      print (t)  # for debugging
    



 
 