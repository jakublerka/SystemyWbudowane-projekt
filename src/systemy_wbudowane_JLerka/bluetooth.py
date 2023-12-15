from machine import UART, Pin
from Motor import PicoGo
from machine import Pin
from ws2812 import NeoPixel
from ST7789 import ST7789
import ujson
import utime


bat = machine.ADC(Pin(26))
temp = machine.ADC(4)

M = PicoGo()
uart = UART(0, 115200)     # init with given baudrate
led = Pin(25, Pin.OUT)
led.value(1)
BUZ = Pin(4, Pin.OUT)
BUZ.value(0)

strip = NeoPixel()
strip.pixels_set(0, strip.BLACK)
strip.pixels_set(1, strip.BLACK)
strip.pixels_set(2, strip.BLACK)
strip.pixels_set(3, strip.BLACK)
strip.pixels_show()

LOW_SPEED    =  30
MEDIUM_SPEED =  50
HIGH_SPEED   =  80

speed = 50
t = 0

while True:
    s=uart.read()
    if(s != None):
        try:
            j=ujson.loads(s)
            #print(j)
            
            command=j.get("Forward")
            if command != None:
                if command == "Down":
                    M.forward(speed)
                    uart.write("{\"State\":\"Forward\"}")
                elif command == "Up":
                    M.stop()
                    uart.write("{\"State\":\"Stop\"}")
                    
            command = j.get("Backward")
            if command != None:
                if command == "Down":
                    M.backward(speed)
                    uart.write("{\"State\":\"Backward\"}")
                elif command == "Up":
                    M.stop()
                    uart.write("{\"State\":\"Stop\"}")
             
            command = j.get("Left")
            if command != None:
                if command == "Down":
                    M.left(20)
                    uart.write("{\"State\":\"Left\"}")
                elif command == "Up":
                    M.stop()
                    uart.write("{\"State\":\"Stop\"}")
                     
            command = j.get("Right")
            if command != None:
                if command == "Down":
                    M.right(20)
                    uart.write("{\"State\":\"Right\"}")
                elif cmd == "Up":
                    M.stop()
                    uart.write("{\"State\":\"Stop\"}")
          
            command = j.get("Low")
            if command == "Down":
                uart.write("{\"State\":\"Low\"}")
                speed = 30

            command = j.get("Medium")
            if cmd == "Down":
                uart.write("{\"State\":\"Medium\"}")
                speed = 50

            cmd = j.get("High")
            if cmd == "Down":
                uart.write("{\"State\":\"High\"}")
                speed = 100
        except:
            print("err")