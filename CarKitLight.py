# Simple KIT car roll back and forth for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 20

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,pixel_order=ORDER)

speed = 30

def kit_forward():
    for j in range(5,num_pixels,1):
        for i in range(num_pixels):
            pixel_value = (0,0,0)
            if i > (j - 5) and i <= j:
                pixel_value = (255,0,0)
            if i == (j - 5):
                pixel_value = (128,0,0)
            if i == (j - 6):
                pixel_value = (64,0,0)
            if i == (j - 7):
                pixel_value = (32,0,0)
            if i == (j - 8):
                pixel_value = (16,0,0)
            pixels[i] = pixel_value
        pixels.show()
        time.sleep(1/speed)

    for i in range(num_pixels):
        pixel_value = (0,0,0)
        if i > (j - 5) and i <= j:
           pixel_value = (255,0,0)
        if i == (j - 5):
           pixel_value = (64,0,0)
        if i == (j - 6):
           pixel_value = (32,0,0)
        if i == (j - 7):
           pixel_value = (16,0,0)
        if i == (j - 8):
           pixel_value = (0,0,0)
        pixels[i] = pixel_value
    pixels.show()
    time.sleep(1/speed)

    for i in range(num_pixels):
        pixel_value = (0,0,0)
        if i > (j - 5) and i <= j:
           pixel_value = (255,0,0)
        if i == (j - 5):
           pixel_value = (64,0,0)
        if i == (j - 6):
           pixel_value = (32,0,0)
        if i == (j - 7):
           pixel_value = (16,0,0)
        if i == (j - 8):
           pixel_value = (0,0,0)
        pixels[i] = pixel_value
    pixels.show()
    time.sleep(1/speed)

    for i in range(num_pixels):
        pixel_value = (0,0,0)
        if i > (j - 5) and i <= j:
           pixel_value = (255,0,0)
        if i == (j - 5):
           pixel_value = (32,0,0)
        if i == (j - 6):
           pixel_value = (16,0,0)
        if i == (j - 7):
           pixel_value = (0,0,0)
        if i == (j - 8):
           pixel_value = (0,0,0)
        pixels[i] = pixel_value
    pixels.show()
    time.sleep(1/speed)

    for i in range(num_pixels):
        pixel_value = (0,0,0)
        if i > (j - 5) and i <= j:
           pixel_value = (255,0,0)
        if i == (j - 5):
           pixel_value = (16,0,0)
        if i == (j - 6):
           pixel_value = (0,0,0)
        if i == (j - 7):
           pixel_value = (0,0,0)
        if i == (j - 8):
           pixel_value = (0,0,0)
        pixels[i] = pixel_value
    pixels.show()
    time.sleep(1/speed)

    for i in range(num_pixels):
        pixel_value = (0,0,0)
        if i > (j - 5) and i <= j:
           pixel_value = (255,0,0)
        pixels[i] = pixel_value
    pixels.show()
    time.sleep(1/speed)



def kit_backward():
    for j in range(num_pixels - 5, -1, -1):
        for i in range(num_pixels):
            pixel_value = (0,0,0)
            if i < (j + 5) and i >= j:
                pixel_value = (255,0,0)
            if i == (j + 5):
                pixel_value = (128,0,0)
            if i == (j + 6):
                pixel_value = (64,0,0)
            if i == (j + 7):
                pixel_value = (32,0,0)
            if i == (j + 8):
                pixel_value = (16,0,0)
            pixels[i] = pixel_value
        pixels.show()
        time.sleep(1/speed)
    pixels[j+8] = (0,0,0)
    pixels[j+7] = (16,0,0)
    pixels[j+6] = (32,0,0)
    pixels[j+5] = (64,0,0)
    pixels.show()
    time.sleep(1/speed)
    pixels[j+7] = (0,0,0)
    pixels[j+6] = (16,0,0)
    pixels[j+5] = (32,0,0)
    pixels.show()
    time.sleep(1/speed)
    pixels[j+6] = (0,0,0)
    pixels[j+5] = (16,0,0)
    pixels.show()
    time.sleep(1/speed)
    pixels[j+5] = (0,0,0)
    pixels.show()
    time.sleep(1/speed)

pixels.fill((0,0,0))
while True:
    kit_forward() 
    kit_backward()

