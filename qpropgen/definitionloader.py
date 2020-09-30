from strictyaml import load, Map, Seq, Str, Bool, Int, Optional, Enum

from qpropgen.errors import QPropgenError

VALUE_SCHEMA = Str() | Bool() | Int()
ACCESS_SCHEMA = Enum(["private", "protected"])
MUTABILITY_SCHEMA = Enum(["constant", "readonly", "readwrite"])
IMPL_SCHEMA = Enum(["plain", "virtual", "pure"])

SCHEMA = Map({
    "class": Str(),
    Optional("includes"): Seq(Str()),
    Optional("baseClass"): Str(),
    Optional("defaults"): Map({
        Optional("type"): Str(),
        Optional("access"): ACCESS_SCHEMA,
        Optional("mutability"): MUTABILITY_SCHEMA,
        Optional("argType"): Str(),
        Optional("impl"): IMPL_SCHEMA,
        Optional("value"): VALUE_SCHEMA,
    }),
    "properties": Seq(
        Map({
            "name": Str(),
            Optional("type"): Str(),
            Optional("access"): ACCESS_SCHEMA,
            Optional("mutability"): MUTABILITY_SCHEMA,
            Optional("argType"): Str(),
            Optional("impl"): IMPL_SCHEMA,
            Optional("value"): VALUE_SCHEMA,
            Optional("varName"): Str(),
            Optional("setterName"): Str()
        }),
    )
})


def load_definition_file(definition_filepath):
    with open(definition_filepath, 'r') as f:
        data = f.read()
    try:
        dct = load(data, SCHEMA)
    except Exception as exc:
        raise QPropgenError("Failed to parse {}: {}".format(definition_filepath, exc))

    if not "type" in dct.get("defaults", {}):
        # Extra validation which cannot be expressed with strictyaml schema
        for prop in dct["properties"]:
            if "type" not in prop:
                raise QPropgenError("Missing type for property {}".format(prop["name"]))

    return dct
