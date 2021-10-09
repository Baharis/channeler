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


def merge(r, g, b, a='', directory='', name='merged.png'):
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
    :param name: fine name of .png file created after the merge
    :type name: str
    """
    o = build_path(directory, name)
    r = Image.open(build_path(directory, r)).convert('RGBA').getchannel(0)
    g = Image.open(build_path(directory, g)).convert('RGBA').getchannel(1)
    b = Image.open(build_path(directory, b)).convert('RGBA').getchannel(2)
    if a is not '':
        a = Image.open(build_path(directory, a)).convert('RGBA').getchannel(3)
        Image.merge('RGBA', (r, g, b, a)).save(o, 'PNG')
    else:
        Image.merge('RGB', (r, g, b)).save(o, 'PNG')


def split(directory='', name=''):
    """
    Split png file into four based on their r/g/b/a channels.

    :param directory: Directory where input and output figures are to be found.
    :type directory: str
    :param name: fine name of .png file created after the merge
    :type name: str
    """
    d = directory
    r_path = build_path(d, path.splitext(name)[0] + '_r.png')
    g_path = build_path(d, path.splitext(name)[0] + '_g.png')
    b_path = build_path(d, path.splitext(name)[0] + '_b.png')
    a_path = build_path(d, path.splitext(name)[0] + '_a.png')
    Image.open(build_path(d, name)).convert('RGBA').getchannel(0).save(r_path)
    Image.open(build_path(d, name)).convert('RGBA').getchannel(1).save(g_path)
    Image.open(build_path(d, name)).convert('RGBA').getchannel(2).save(b_path)
    Image.open(build_path(d, name)).convert('RGBA').getchannel(3).save(a_path)


if __name__ == '__main__':
    n = 'example{}.png'
    split(name='example.png')
    merge(n.format('_g'), n.format('_b'), n.format('_r'), a=n.format('_a'))
