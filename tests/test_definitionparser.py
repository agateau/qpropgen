import pytest

from qpropgen.definitionparser import parse_definition_string
from qpropgen.errors import ParseError


def test_load_ok():
    data = """
class: Person
properties:
- name: firstName
  type: QString
- name: lastName
  type: QString
- name: birthDate
  type: QDateTime
"""

    dct = parse_definition_string(data)
    assert dct["class"] == "Person"


def test_invalid_definition_file():
    data = "clas: Person"
    with pytest.raises(ParseError):
        parse_definition_string(data)


def test_type_set_in_defaults_field():
    # If `type` is set in defaults, it does not have to be set for each properties
    data = """
class: Sound
defaults:
    type: qreal
properties:
    - name: p1
    - name: p2
"""

    dct = parse_definition_string(data)
    assert dct["class"] == "Sound"


def test_type_not_in_defaults_fails():
    # If `type` is not set in defaults, it must be set for each properties
    data = """
class: Sound
properties:
    - name: p1
    - name: p2
"""

    with pytest.raises(ParseError):
        parse_definition_string(data)
