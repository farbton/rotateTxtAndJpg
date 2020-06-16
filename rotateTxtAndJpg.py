import argparse
import os
import sys

from manipulate import Manipulate

def main():
    parser = argparse.ArgumentParser(description='rotate bbox and img')
    parser.add_argument('-s', help='source directory of orginal images and txt files', default='source')
    parser.add_argument('-o', help='target directory of rotated images and txt files', default='out')
    parser.add_argument('-a', help='angle for rotation', required=True)
    args = parser.parse_args()

    source_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.s)
    if not os.path.exists(source_dir):
        print('Provide the correct folder for images')
        sys.exit()

    out_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.o)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if not os.access(out_dir, os.W_OK):
        print("%s folder is not writeable.")
        sys.exit()

    manipulate = Manipulate(source_dir=source_dir, out_dir=out_dir, angle=args.a)
    manipulate.start()


if __name__ == "__main__":
    main()
