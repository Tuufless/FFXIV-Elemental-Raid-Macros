import os
from PIL import Image

def crop(directory):
    for path, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".jpg"):
                filename = os.path.join(path, f)
                img = Image.open(filename)
                imgWidth, imgHeight = img.size

                if imgWidth == imgHeight + 1 and imgHeight in [500, 750, 1000]:
                    left = 0
                    top = 0
                    width = imgHeight
                    height = imgHeight

                    box = (left, top, left + width, top + height)

                    print("Cropping " + f)

                    area = img.crop(box)
                    area.save(os.path.join(path, f), 'jpeg')


if __name__ == "__main__":
    """
    Handles a bug in Figma export where there is a single column of white pixels on the right.
    """
    crop(os.path.join(os.getcwd(), "images", "ultimates"))