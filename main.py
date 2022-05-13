import cv2
import os


here    = os.path.dirname(os.path.realpath(__file__))
chars   = " -.,~:=*!;#$@"
res_x = 200
res_y = 50

print("initializing cam")
cam = cv2.VideoCapture(1)
print("initialized cam")


def get_image():
    result, image = cam.read()
    if result:
        return image, 1
    return 0, 0

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

while True:
    image = get_image()
    if (image[1]):
        image = image[0]
        cv2.imshow("image", image)
        cv2.waitKey(1)
        image = cv2.resize(image, (res_x, res_y))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(image)
