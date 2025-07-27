"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    #filename = get_file()
    image = SimpleImage(DEFAULT_FILE)

    # Show the image before the transform
    image.show()
    image = SimpleImage(DEFAULT_FILE)


    # Apply the filter
    # Write code here
    # Show the image after the transform


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()