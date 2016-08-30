# Quality Assurance
QA is a different discipline from a software developers, however software developers must be exposed to it, since testing is essential.

Application can be devided into two categories:

- Logic
- Representation

*Logic* is responsible for actions with a data. *Representation* is an interface to particular pieces of the logic. Logic is always hidden from a user, user interacts with the representation layer. In practice these parts can be labeled as a *backend* and a *frontend* respectively.


## Types of Tests
There are two broad categories: *unit testing* and *integration testing*.

#### Unit Testing
Unit testing is a precise test suite of a module, a unit, a component. It exists to make sure that module functions as intended. Unit testing mostly and usually used on a *logic* side.

#### Integration Testing
Integration tests is a tests for integration between modules, units, components. It exists to make sure that modules interacts with each other as intended. Integration testing is useful on both, a *logic* and a *representation*, sides.
