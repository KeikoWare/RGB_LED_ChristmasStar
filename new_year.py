# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import random

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 100
star_pixels = 72

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,pixel_order=ORDER)
pBr = 128 # 92 # Pixel Brightness RED
pBg = 128 # 82  # Pixel Brightness GREEN
pBb = 128 # 62  # Pixel Brightness BLUE
tL = 0.2 # length of the twinkle

tSleep = 0.05

rings = [[   6,   18,   30,   42,   54   ,66],
[5, 7,17,19,29,31,41,43,53,55,65,67],
[4, 8,16,20,28,32,40,44,52,56,64,68],
[3, 9,15,21,27,33,39,45,51,57,63,69],
[2,10,14,22,26,34,38,46,50,58,62,70],
[1,11,13,23,25,35,37,47,49,59,61,71],
[0,   12,   24,   36,   48,   60   ]]

tops = [[66,67,68,69,70,71,0,1,2,3,4,5],
[6,7,8,9,10,11,12,13,14,15,16,17],
[18,19,20,21,22,23,24,25,26,27,28,29],
[30,31,32,33,34,35,36,37,38,39,40,41],
[42,43,44,45,46,47,48,49,50,51,52,53],
[54,55,56,57,58,59,60,61,62,63,64,65]]

pixels.fill((0,0,0))
pixels.show()


def twinkle():
    pixels.fill((0, 0, 0))
    for i in range(star_pixels):
        pixels[i]  = (pBr, pBg, pBb)
    pixels.show()
    stars = random.randint(1,7)
    my_randoms = random.sample(range(72), stars)
    for j in my_randoms:
        pixels[j] = (255,255,255) # Set Twinkle brightness
        pixels.show() # Show Twinkle
        time.sleep(tL) # Show Time
        pixels[j] = (pBr, pBg, pBb) # Set normal britghness again
        pixels.show() # Hide Twinkle
        pL = random.uniform(0.01,1.50) # Calculate Pause Time before next Twinkle
        time.sleep(pL) # Twinkle Pause


def circle(): # Wheel of fortune :)
    top = 0
    sleeptime = 0.15
    result = random.randint(14,25)
    for k in range(result):
        circle_step(top)
        top = top + 1
        if top > 5:
            top = 0
        sleepTime = 0.15
        if k + 4 > result:
            sleeptime = 0.15 * (k - (result - 5))
        time.sleep(sleeptime)
    pixels.fill((0, 0, 0))
    for i in range(star_pixels):
        pixels[i]  = (pBr, pBg, pBb)
    pixels.show()
    time.sleep(0.3)
    circle_step(top)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    for i in range(star_pixels):
        pixels[i]  = (pBr, pBg, pBb)
    pixels.show()
    time.sleep(0.3)
    circle_step(top)
    time.sleep(0.8)
    pixels.fill((0, 0, 0))
    for i in range(star_pixels):
        pixels[i]  = (pBr, pBg, pBb)
    pixels.show()
    time.sleep(0.3)
    circle_step(top)
    time.sleep(0.8)
    pixels.fill((0, 0, 0))
    for i in range(star_pixels):
        pixels[i]  = (pBr, pBg, pBb)
    pixels.show()
    time.sleep(0.3)
    circle_step(top)
    time.sleep(0.8)


def circle_step(top):
    if top < 0 or top > 5:
        top = 0
    pixels.fill((0, 0, 0))
    for k in range(star_pixels):
        pixels[k]  = (pBr, pBg, pBb)
    if top < 5 :
        for j in range(12):
            p = top * 12 + j + 6
            pixels[p] = (255, 255, 255)
    else:
        for j in range(6):
            p = top * 12 + j + 6
            pixels[p] = (255, 255, 255)
        for j in range(6):
            pixels[j] = (255, 255, 255)
    pixels.show()


def colorwheel(pos):
    # Input a value 0 to 255 to get a color value. The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    pixels.fill((0, 0, 0))
    for j in range(2000):
        for i in range(star_pixels):
            pixel_index = (i * 256 // star_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def shooting_star(ShootingStarColor):
    #tail up 
    pixels.fill((0, 0, 0))
    tSleep = 0.01
    tail = range(99, 71, -1)
    for i in tail:
        if i < 97:
            pixels[i+3] = (0,0,0)
        pixels[i] = ShootingStarColor
        if i < 99:
            pixels[i+1] = ShootingStarColor
        if i < 98:
            pixels[i+2] = ShootingStarColor
        pixels.show()
        time.sleep(tSleep)
    pixels[i+2] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    pixels[i+1] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    tSleep = 0.05
    #star build up
    star_on_up(ShootingStarColor)
    time.sleep(tSleep)
    star_off_up()
    time.sleep(tSleep)
    star_on_up(ShootingStarColor)
    time.sleep(tSleep)
    star_off_up()
    time.sleep(tSleep)
    star_on_up(ShootingStarColor)
    time.sleep(tSleep)
    star_off_up()
    time.sleep(tSleep)
    star_on_up(ShootingStarColor)
    time.sleep(tSleep)
    star_off_up()
    time.sleep(tSleep)
    star_on_up(ShootingStarColor)
    time.sleep(tSleep)
    star_off_up()


def star_on_up(ShootingStarColor):
    global tSleep
    for i in rings[0]:
        pixels[i] = ShootingStarColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[1]:
        pixels[i] = ShootingStarColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[2]:
        pixels[i] = ShootingStarColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[3]:
        pixels[i] = ShootingStarColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[4]:
        pixels[i] = ShootingStarColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[5]:
        pixels[i] = ShootingStarColor
    pixels.show()
    time.sleep(0.01)
    for i in rings[6]:
        pixels[i] = ShootingStarColor
    pixels.show()


def star_off_up():
    global tSleep
    for i in rings[0]:
        pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    for i in rings[1]:
        pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    for i in rings[2]:
        pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    for i in rings[3]:
        pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    for i in rings[4]:
        pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(tSleep)
    for i in rings[5]:
        pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(0.01)
    for i in rings[6]:
        pixels[i] = (0,0,0)
    pixels.show()

def star_pulse(PulseColor):
    global tSleep
    tmp = tSleep
    tSleep = 0.1
    pixels.fill((0, 0, 0))
    for i in rings[0]:
        pixels[i] = PulseColor
    for i in rings[1]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[0]:
        pixels[i] = (0,0,0)
    for i in rings[2]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[1]:
        pixels[i] = (0,0,0)
    for i in rings[2]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[2]:
        pixels[i] = (0,0,0)
    for i in rings[4]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[3]:
        pixels[i] = (0,0,0)
    for i in rings[5]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[4]:
        pixels[i] = (0,0,0)
    for i in rings[6]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    time.sleep(tSleep)
    for i in rings[6]:
        pixels[i] = (0,0,0)
    for i in rings[4]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[5]:
        pixels[i] = (0,0,0)
    for i in rings[3]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[4]:
        pixels[i] = (0,0,0)
    for i in rings[2]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[3]:
        pixels[i] = (0,0,0)
    for i in rings[1]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    for i in rings[2]:
        pixels[i] = (0,0,0)
    for i in rings[0]:
        pixels[i] = PulseColor
    pixels.show()
    time.sleep(tSleep)
    time.sleep(tSleep)
    tSleep = tmp

    
def kill_star():
    my_randoms = list(range(star_pixels))
    random.shuffle(my_randoms)
    for i in my_randoms:
        pixels[i] = (0,0,0)
        pixels.show()
        time.sleep(tSleep)


colorIndex = 0
while True:    
    # RAINBOW
    rainbow_cycle(0.001)
    kill_star()
    # PULSE
    for k in range(0,500,50):
        colorIndex = ((colorIndex + 32) & 255)
        star_pulse(colorwheel(colorIndex))
    # SHOOTING STAR
    for k in range(0,250,10):
        colorIndex = ((colorIndex + 128 + random.randint(0,10)) & 255)
        shooting_star(colorwheel(colorIndex))
