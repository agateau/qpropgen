from qpropgen.main import ClassDefinition, parse_definition_file


def test_classdefinition():
    dct = {
        "class": "Person",
        "properties": [
            {
                "name": "firstName",
                "type": "QString",
            }
        ]
    }
    cd = ClassDefinition("person.yaml", dct)
    assert len(cd.properties) == 1
    firstname_prop = cd.properties[0]
    assert firstname_prop["setterName"] == "setFirstName"
    assert firstname_prop["argType"] == "const QString&"
    assert firstname_prop["varName"] == "mFirstName"


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

    parse_definition_file(testpath)
