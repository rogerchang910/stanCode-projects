"""
File: blur.py
Name: Roger(Yu-Ming) Chang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage

BLUR_TIMES = 5


def main():
    """
    An image will become blurred after this function.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_TIMES):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: (SimpleImage), an original image.
    :return: (SimpleImage), a blurred image of img.
    """
    blurred = img.blank(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x + i
                    pixel_y = y + j

                    if 0 <= pixel_y < img.height:
                        if 0 <= pixel_x < img.width:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1

            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count

    return blurred


if __name__ == '__main__':
    main()
