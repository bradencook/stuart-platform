from servo import Servo
from machine import Pin, ADC
import utime

s1 = Servo(11)
s2 = Servo(12)
s3 = Servo(13)
    
xAxis = ADC(Pin(26)) # avg = 32400 max = 65500 min = 155
yAxis = ADC(Pin(27)) # avg = 33600 max = 65500 min = 128

button = Pin(16, Pin.IN, Pin.PULL_UP)

    
def write(xValue, yValue):
    if xValue > 30:
        xValue = 30
    elif xValue < -30:
        xValue = -30
        
    if yValue > 30:
        yValue = 30
    elif yValue < -30:
        yValue = -30
        
    s1.write(30 + 0.5 * yValue - 0.866 * xValue)
    s2.write(30 + 0.5 * yValue + 0.866 * xValue)
    s3.write(30 - yValue)
    
def joy():   
    while button.value():
        xValue = 30 *(xAxis.read_u16() / 65500 - 0.5)
        yValue = 30 *(yAxis.read_u16() / 65500 - 0.5)
        
        write(xValue, yValue)
        
write(0,0)