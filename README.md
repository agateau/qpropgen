# qpropgen

A tool to generate QML-friendly QObject-based C++ classes from class definition
files.

## Quick Intro

Declaring properties in a QObject class can be tedious: there is quite a lot of
boilerplate code to write. qpropgen goal is to write this boilerplate for you.

Suppose we want to create a `Person` class, with `firstName`, `lastName` and
`birthDate` properties.

First we create a class definition file named `person.yaml` with the following
content:

    class: Person
    properties:
        - name: firstName
          type: QString
        - name: lastName
          type: QString
        - name: birthDate
          type: QDateTime

Next, we generate its header and implementation with `qpropgen person.yaml`

Now we can use `person.h` and `person.cpp` in our code. The filenames are
defined from the filename of the class definition.

Note: in practice, you probably want to inherit from the generated classes to
implement other aspects of the class to create and/or to override getters and
setters.

## Syntax of class definition files

A class definition file must contain the following fields:

- `class`: the name of the class to generate.

- `properties`: the list of its properties (see below).

It may also contain the following fields:

- `includes`: a list of files to include in the header.

- `baseClass`: name of the class to inherit from. Defaults to `QObject`.

- `defaults`: default values for some property attributes (see below).

### The `properties` field

`properties` is an array of property definitions.

A property definition must contain the following fields:

- `type`
- `name`

It may contain the following fields:

- `access`: Can be `private` or `protected`. Defines the access modifier for
  the generated member variables. Defaults to `private`.

- `mutability`: One of `constant`, `readonly`, `readwrite`. Defaults to
  `readwrite`.

- `argType`: The type of the setter argument. If not set qpropgen uses const
  references for types which are not pointers and not known scalars (int, bool,
  qreal).

- `setterName`: Name of the setter. Defaults to `set<Name>`, so the setter of
  a property named `foo` will be named `setFoo`.

- `varName`: Name of the variable backing the property. Defaults to `m<Name>`,
  so the variable of a property named `foo` will be named `mFoo`.

- `impl`: One of `plain` (getter and setter), `virtual` (virtual getter and
  setter) or `pure` (virtual pure getter and setter).

- `value`: The default value of the property.

### The `defaults` field

Adding a field to the `defaults` object lets you define default values for all
properties.

For example you can define that all properties are of type `qreal` by default
with:

```
defaults:
    type: qreal
```

Of course some fields like `name` should not have a default.

## Build system integration

The `cmake/qpropgen.cmake` can be included in your project to integrate
qpropgen in. It takes care of finding the `qpropgen` executable and provides a
`qpropgen()` CMake function.

This CMake function lets you define .yaml files to process. For example:


```cmake
set(prj_SRCS main.cpp)
qpropgen(prj_QPROPGEN foo.yaml bar.yaml)
add_executable(prj ${prj_SRCS} ${prj_QPROPGEN})
```

## Examples

The `examples/` directory contains examples of the various settings. The
produced executable does nothing, but you can look in the build directory at
the .h and .cpp files produced by qpropgen during the build.

## Tests

The project currently lacks real unit tests, so the examples serve as tests:
the `./tests.sh` script can be run to build the examples.

## Trivia

I started this project when I was working on the [SFXR-Qt][] sound generator (a
QtQuick port of [SFXR][]), and was finding it too tedious to declare all the
properties necessary to represent sounds :)

[SFXR-Qt]: https://github.com/agateau/sfxr-qt
[SFXR]: http://www.drpetter.se/project_sfxr.html
