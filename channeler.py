from os import path
from PIL import Image


def build_path(*path_elements):
    """
    Return an absolute path to the location based on provided strings.
    Substitute tilde '~' with home directory.

    :Example:

    >>> build_path('image.png')
    '/current/working/directory/image.png'
    >>> build_path('~', 'Pictures/image.png')
    '/home/directory/Pictures/image.png'

    :param path_elements: path elements to be joined
    :type path_elements: str
    :return: absolute path to the given location
    :rtype: str
    """
    return path.abspath(path.expanduser(path.join(*path_elements)))


def merge(r, g, b, a='', path='', out='merged.png'):
    """
    Merge three (or four) png images into one using their r/g/b(/a) channels.

    :param path: Directory where input and output figures are to be found.
    :type path: str
    :param r: file name of .png file holding the red channel for desired merge
    :type r: str
    :param g: file name of .png file holding the green channel for desired merge
    :type g: str
    :param b: file name of .png file holding the blue channel for desired merge
    :type b: str
    :param a: file name of .png file holding the alpha channel, if necessary
    :type a: str
    :param out: fine name of .png file created after the merge
    :type out: str
    :return: None
    :rtype: None
    """
    o = build_path(path, out)
    r = Image.open(build_path(path, r)).convert('RGBA').getchannel(0)
    g = Image.open(build_path(path, g)).convert('RGBA').getchannel(1)
    b = Image.open(build_path(path, b)).convert('RGBA').getchannel(2)
    if a is not '':
        a = Image.open(build_path(path, a)).convert('RGBA').getchannel(3)
        Image.merge('RGBA', (r, g, b, a)).save(o, 'PNG')
    else:
        Image.merge('RGB', (r, g, b)).save(o, 'PNG')


if __name__ == '__main__':
    n = 'example{}.png'
    merge(n.format('_r'), n.format('_g'), n.format('_b'))
