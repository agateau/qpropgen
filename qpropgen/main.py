"""
Generate QML-friendly QObject-based C++ classes from class definition files
"""
import argparse
import os
import sys

from jinja2 import Environment, PackageLoader

from qpropgen.classdefinition import HEADER_EXT, IMPL_EXT, ClassDefinition
from qpropgen.definitionloader import load_definition_file
from qpropgen.errors import QPropgenError


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    parser.add_argument('-d', '--directory', dest='directory',
                        default='.',
                        help='generate files in DIR', metavar='DIR')

    parser.add_argument('class_definition')

    args = parser.parse_args()

    try:
        dct = load_definition_file(args.class_definition)
        definition = ClassDefinition(args.class_definition, dct)

        env = Environment(loader=PackageLoader('qpropgen', 'templates'))

        for ext in HEADER_EXT, IMPL_EXT:
            out_path = os.path.join(args.directory, definition.filename_we + ext)
            template = env.get_template('template{}'.format(ext))
            definition.generate_file(template, out_path)
    except QPropgenError as exc:
        print(exc)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
# vi: ts=4 sw=4 et
