from PIL import Image
import os
import pygame
import pygame.camera

pygame.camera.init()
camlist = pygame.camera.list_cameras()
print(f"cams {camlist}")
cam = pygame.camera.Camera(camlist[0], (640, 480))
cam.start()
image = cam.get_image()
pygame.image.save(image, "filename.jpg")

def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


image = Image.open("filename.jpg")
level = calculate_brightness(image)
print("%s\t%s" % ("image", level))
os.system(f"xrandr --output eDP --brightness {level+0.2}")

# os.remove("filename.jpg")