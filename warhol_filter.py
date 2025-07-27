"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba.png'

def main():
    image = SimpleImage(PATCH_NAME)
    width_patch = image.width
    height_patch = image.height
    make_recolored_patch (1.5, 1, 1.5)

    
    
    # add patch color
    #
    # change patch color
    #
    # This is an example which should generate a pinkish patch"""


def make_recolored_patch(red_scale,green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        average = pixel.red + pixel.blue + pixel.green // 3
        pixel.red = pixel.red*red_scale
        pixel.green = pixel.green*green_scale
        pixel.blue = pixel.blue*blue_scale
    patch.show()
    return patch

if __name__ == '__main__':
    main()