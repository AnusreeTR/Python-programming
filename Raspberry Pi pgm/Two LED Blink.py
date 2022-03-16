from machine import Pin
import utime

led1 = Pin(14, Pin.OUT)
led2 = Pin(9, Pin.OUT)
while True:
  led1.toggle()
  utime.sleep(1)
  led2.toggle()
  utime.sleep(1)
