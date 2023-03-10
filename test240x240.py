import ST7789
from PIL import Image
from time import sleep

'''
Screen used is 240x240

GPIO is all in the ST7789 init object

port=0 : RPi has 2 SPI ports. We are using port 0. SDA on the screen is attached to MOSI (GPIO 10)

cs=1   : CS on screen attached to SPI0 CE1 (GPIO 7)

rst=25 : reset on screen attached to GPIO 25

backlight=19 : Backlight on screen attached to GPIO 19
'''

display=ST7789.ST7789(port=0,cs=1,rst=25,dc=9,backlight=19,spi_speed_hz=80 * 1000 * 1000)
display._spi.mode=3
display.reset()
display._init()
# Display a Color for 2 seconds
image=Image.new('RGB',(240,240),(0,0,225))  #('RGB',(240,240),(r,g,b))
display.display(image)
sleep(2)
image=Image.open("images/cat.jpg")
image=image.resize((240,240),resample=Image.LANCZOS)
display.display(image)
