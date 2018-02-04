# qpropgen

Generates classes containing Qt properties.

## Usage

### Create a class definition

Create a class definition, using the following syntax:

    class:
        name: Person
        access: private|protected (defaults to private)
    properties:
        - <property definition>

A property definition must have the following fields:

- `type`
- `name`

It may have the following fields:

- `mutability`: One of `constant`, `readonly`, `readwrite`. Defaults to
  `readwrite`.

- `arg_type`: The type of the setter argument. If not set qpropgen uses const
  refs for types which are not pointers and not known scalars (int, bool,
  qreal)

- `setter_name`: Name of the setter. Defaults to `set<Name>`, so the setter of
  a property named `foo` will be `setFoo`.

- `var_name`: Name of the variable backing the property. Defaults to `m<Name>`,
  so the variable of a property named `foo` will be `mFoo`.

### Generate the class

Generate it with `qpropgen person.yaml`
