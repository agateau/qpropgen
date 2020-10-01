from strictyaml import load, Map, Seq, Str, Bool, Int, Optional, Enum

from qpropgen.errors import ParseError

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


def parse_definition_string(data):
    try:
        dct = load(data, SCHEMA)
    except Exception as exc:
        raise ParseError(f"Failed to parse definition file: {exc}")

    if not "type" in dct.get("defaults", {}):
        # Extra validation which cannot be expressed with strictyaml schema
        for prop in dct["properties"]:
            if "type" not in prop:
                raise ParseError("Missing type for property {}".format(prop["name"]))

    return dct
