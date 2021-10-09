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


def merge(directory, r, g, b, a='', out='merged.png'):
    """
    Merge three (or four) png images into one using their r/g/b(/a) channels.

    :param directory: Directory where input and output figures are to be found.
    :type directory: str
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
    o = build_path(directory, out)
    r = Image.open(build_path(directory, r)).getchannel(0)
    g = Image.open(build_path(directory, g)).getchannel(1)
    b = Image.open(build_path(directory, b)).getchannel(2)
    if a is not '':
        a = Image.open(build_path(directory, a)).getchannel(3)
        Image.merge('RGBA', (r, g, b, a)).save(o, 'PNG')
    else:
        Image.merge('RGB', (r, g, b)).save(o, 'PNG')


if __name__ == '__main__':
    n = 'CpltMap_Mo35a{}_Pm-3_gnu.png'
    merge('~', r=n.format('X'), g=n.format('Y'), b=n.format('Z'), out=n)
