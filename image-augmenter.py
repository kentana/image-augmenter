import sys
import os
from PIL import Image
import tensorflow as tf
import numpy as np

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


def dst_image_path(filename):
    """
    returns dst image's path from filename.
    """

    return 'dst/' + filename


def permitted_image(filename):
    """
    reports image is permitted.
    """

    ext = filename.split('.')[-1]
    return ext in EXTS


def lighten(image):
    """
    lighten image.
    """
    return tf.image.adjust_brightness(image, 0.5)


def darken(image):
    """
    darken image.
    """
    return tf.image.adjust_brightness(image, -0.5)


def flip_up_down(image):
    """
    flip image vertically.
    """
    return tf.image.flip_up_down(image)


def flip_left_right(image):
    """
    flip image horizontally.
    """
    return tf.image.flip_left_right(image)


def high_contrast(image):
    """
    up image contrast.
    """
    return tf.image.adjust_contrast(image, 90)


def low_contrast(image):
    """
    down image contrast.
    """
    return tf.image.adjust_contrast(image, 0.2)


def augment(image):
    """
    augments image.
    """
    return [
        lighten(image),
        darken(image),
        flip_up_down(image),
        flip_left_right(image),
        high_contrast(image),
        low_contrast(image),
    ]


def generate_dst_filename(image, sufix):
    """
    generates dst file name.
    """
    filepath = image.filename
    filename = filepath.split('/')[-1]
    name, ext = filename.split('.')
    return f'{name}_{sufix}.{ext}'


def save_image(image, filename):
    """
    saves image.
    """
    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        tf.train.start_queue_runners(coord=coord)
        for i in range(4):
            img = sess.run(image)
            Image.fromarray(np.uint8(img)).save(dst_image_path(filename))


def main():
    images = get_images()
    augmented_images = [augment(i) for i in images]

    for idx, imgs in enumerate(augmented_images):
        image = images[idx]
        for i, img in enumerate(imgs):
            save_image(img, generate_dst_filename(image, i))


if __name__ == '__main__':
    main()
