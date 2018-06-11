import sys
import os
from PIL import Image
import tensorflow as tf

# exts.
# image-augmenter handles only png and jpg.
EXTS = ['png', 'jpg']


def get_images():
    """
    gets images in src directory.
    """

    src_path = os.getcwd() + '/src'

    # get all images.
    src_files = os.listdir(src_path)
    image_paths = [image_path(i) for i in src_files if permitted_image(i)]
    images = [Image.open(i) for i in image_paths]

    return images


def image_path(filename):
    """
    returns image's path from filename.
    """

    return 'src/' + filename


def permitted_image(filename):
    """
    reports image is permitted.
    """

    ext = filename.split('.')[-1]
    return ext in EXTS


def lighten(image):
    # TODO: lighten!
    return tf.image.random_brightness(image, 1)


def darken(image):
    # TODO: darken!
    return tf.image.random_brightness(image, 2)


def flip_up_down(image):
    return tf.image.random_flip_up_down(image)


def flip_left_right(image):
    return tf.image.random_flip_left_right(image)


def high_contrast(image):
    # TODO: high contrast!!
    return tf.image.random_contrast(image, 90, 100)


def low_contrast(image):
    # TODO: low contrast!!
    return tf.image.random_contrast(image, 0, 1)


def main():
    images = get_images()
    print('images')
    print(images)
    lighten_images = [lighten(i) for i in images]
    print('images')
    print(images)
    print('lightn images')
    print(lighten_images)

    for i in lighten_images:
        i.show()
        i.save('lighten.jpg')


if __name__ == '__main__':
    main()
