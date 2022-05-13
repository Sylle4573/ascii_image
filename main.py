import cv2
import os

### - Edit this if needed - ###
chars   = " -.,~:=*!;#$@"   # The color ascii representation. Change if needed. More to the right means brighter.
res   = (200, 50)           # Recommended to keep as is due to performance issues at higher resolutions!
webcam  = 1                 # The camera to use
### - Edit this if needed - ###


here = os.path.dirname(os.path.realpath(__file__))
print("initializing cam")
cam = cv2.VideoCapture(webcam)
print("initialized cam")


# Captures image from webcam
def get_image():
    result, image = cam.read()
    if result:
        return image, 1
    return 0, 0

# Displays image in ascii
def display_image(img):
    line = ""
    for x in img:
        for y in x:
            value   = round(y / (255 / 12))
            char    = chars[value]
            line    += char
        line += "\n"
    os.system("cls")
    print(line)

# Main loop
def main():
    while True:
        image = get_image()
        if (image[1]):
            image = image[0]
            cv2.imshow("image", image)
            cv2.waitKey(1)
            image = cv2.resize(image, (res[0], res[1]))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        display_image(image)

main()
# If any of it needs better explanation, just message me.
# I've got nothing better to do.
