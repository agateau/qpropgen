# qpropgen

Generates classes containing Qt properties.

## Quick Intro

Suppose we want to create a Person class, with firstName, lastName and
birthDate properties.

First create a class definition file named person.yaml with the following
content:

    class:
        name: Person
    properties:
        - name: firstName
          type: QString
        - name: lastName
          type: QString
        - name: birthDate
          type: QDateTime

Next, generate its header and implementation with `qpropgen person.yaml`

You can now use person.h and person.cpp in your code. The filenames are defined
from the filename of the class definition.

## Class definition syntax

A class definition contains the following fields:

- `class`
- `properties`

### `class`

`class` must contains the following fields:

- `name`: Class name

It may also contain the following fields:

- `access`: Can be `private` or `protected`. Access modifier for generated
  member variables. Defaults to `private`.

### `properties`

`properties` is an array of property definitions.

A property definition must contain the following fields:

- `type`
- `name`

It may have the following fields:

- `mutability`: One of `constant`, `readonly`, `readwrite`. Defaults to
  `readwrite`.

- `argType`: The type of the setter argument. If not set qpropgen uses const
  refs for types which are not pointers and not known scalars (int, bool,
  qreal)

- `setter_name`: Name of the setter. Defaults to `set<Name>`, so the setter of
  a property named `foo` will be `setFoo`.

- `var_name`: Name of the variable backing the property. Defaults to `m<Name>`,
  so the variable of a property named `foo` will be `mFoo`.

- `impl`: One of `plain` (getter and setter), `virtual` (virtual getter and
  setter) or `pure` (virtual pure getter and setter)

## Build system integration

qpropgen comes with CMake support. Look at `examples/CMakeLists.txt` for
details.
