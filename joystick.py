from machine import Pin, ADC
from servo import Servo
import utime

s1 = Servo(11)
s2 = Servo(12)
s3 = Servo(13)

xAxis = ADC(Pin(26)) # avg = 32400 max = 65500 min = 155
yAxis = ADC(Pin(27)) # avg = 33600 max = 65500 min = 128

button = Pin(16, Pin.IN, Pin.PULL_UP)

def all(angle):
    s1.write(angle)
    s2.write(angle + 3)
    s3.write(angle)
    
    
while True:
    xValue = 20 *(xAxis.read_u16() / 65500 - 0.5)
    yValue = 20 *(yAxis.read_u16() / 65500 - 0.5)
    
    s1.write(22.5 + 0.5 * yValue - 0.866 * xValue)
    s2.write(22.5 + 0.5 * yValue + 0.866 * xValue)
    s3.write(23.5 - yValue)
