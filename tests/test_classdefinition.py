from qpropgen.classdefinition import ClassDefinition


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
