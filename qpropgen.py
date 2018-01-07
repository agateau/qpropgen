#!/usr/bin/env python3
import argparse
import os
import sys

import yaml

from jinja2 import Environment, PackageLoader


__appname__ = 'qpropgen'
__version__ = '0.1.0'
__license__ = 'Apache 2.0'

DESCRIPTION = """\
Generate QML property-based headers and implementation
"""

NO_CONST_REF_ARG_TYPES = {'int', 'bool', 'qreal'}


def generate_file(template, filename, class_def, properties, directory):
    filepath = os.path.join(directory, filename)

    args = dict(
        filename=filename,
        header=class_def['class']['header'],
        class_name=class_def['class']['name'],
        properties=properties,
    )

    with open(filepath, 'w') as f:
        f.write(template.render(**args))


def create_property_def(property_def):
    """Adds extra fields to property_def"""
    camelcase_name = property_def['name'][0].upper() + property_def['name'][1:]
    setter_name = 'set' + camelcase_name

    type_ = property_def['type']
    need_constref = type_ not in NO_CONST_REF_ARG_TYPES and type_[-1] != '*'
    if need_constref:
        arg_type = 'const {}&'.format(type_)
    else:
        arg_type = type_

    try:
        var_name = property_def['var_name']
    except KeyError:
        var_name = 'm' + camelcase_name

    property_def.update(
        setter_name=setter_name,
        arg_type=arg_type,
        var_name=var_name,
    )
    return property_def


def main():
    parser = argparse.ArgumentParser()
    parser.description = DESCRIPTION

    parser.add_argument('-d', '--directory', dest='directory',
                        default='.',
                        help='generate files in DIR', metavar='DIR')

    parser.add_argument('class_definition')

    args = parser.parse_args()

    with open(args.class_definition, 'r') as f:
        class_def = yaml.load(f)

    properties = [create_property_def(x) for x in class_def['properties']]

    env = Environment(loader=PackageLoader('qpropgen', 'templates'))

    template = env.get_template('header.h')
    filename = class_def['class']['header']
    generate_file(template, filename, class_def, properties, args.directory)

    template = env.get_template('impl.cpp')
    filename = class_def['class']['impl']
    generate_file(template, filename, class_def, properties, args.directory)

    return 0


if __name__ == '__main__':
    sys.exit(main())
# vi: ts=4 sw=4 et
