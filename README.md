# qpropgen

Generates classes containing Qt properties.

## Usage

Create a class definition, using the following syntax:

    class:
        name: Person
    properties:
        - type: QString
          name: firstName
        - type: QString
          name: lastName
        - type: QDateTime
          name: birthDate
          value: (optional)
          arg_type: (optional)
          setter_name: (optional)

Generate it with `qpropgen person.yaml`
