from qpropgen.definitionloader import load_definition_file


def test_parse_definition(tmpdir):
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

    load_definition_file(testpath)
