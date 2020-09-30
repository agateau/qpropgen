import strictyaml

from qpropgen.errors import QPropgenError


def load_definition_file(definition_filepath):
    with open(definition_filepath, 'r') as f:
        data = f.read()
    try:
        return strictyaml.load(data)
    except Exception as exc:
        raise QPropgenError("Failed to parse {}: {}".format(definition_filepath, exc))
