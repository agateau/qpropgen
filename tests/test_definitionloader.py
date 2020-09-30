import pytest

from qpropgen.definitionloader import load_definition_file
from qpropgen.errors import QPropgenError


def test_load_ok(tmpdir):
    testpath = tmpdir / "test.yaml"
    with open(testpath, "w") as f:
        f.write(
            """
class: Person
properties:
- name: firstName
  type: QString
- name: lastName
  type: QString
- name: birthDate
  type: QDateTime
            """
        )

    dct = load_definition_file(testpath)
    assert dct["class"] == "Person"


def test_invalid_definition_file(tmpdir):
    testpath = tmpdir / "test.yaml"
    with open(testpath, "w") as f:
        f.write(
            """
clas: Person
            """
        )

    with pytest.raises(QPropgenError):
        load_definition_file(testpath)


def test_type_set_in_defaults_field(tmpdir):
    # If `type` is set in defaults, it does not have to be set for each properties
    testpath = tmpdir / "test.yaml"
    with open(testpath, "w") as f:
        f.write(
            """
class: Sound
defaults:
    type: qreal
properties:
    - name: p1
    - name: p2
            """
        )

    dct = load_definition_file(testpath)
    assert dct["class"] == "Sound"


def test_type_not_in_defaults_fails(tmpdir):
    # If `type` is not set in defaults, it must be set for each properties
    testpath = tmpdir / "test.yaml"
    with open(testpath, "w") as f:
        f.write(
            """
    class: Sound
    properties:
        - name: p1
        - name: p2
                """
            )

    with pytest.raises(QPropgenError):
        load_definition_file(testpath)
