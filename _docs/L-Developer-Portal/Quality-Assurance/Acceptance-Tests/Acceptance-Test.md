# Acceptance Test

Acceptance tests exercise application features on an end-to-end basis from the perspective of the user.

* BDD Acceptance tests verify the behaviour and features in the running `CluedIn.App`.

  Tests are defined using a `Given`, `When`, `Then` syntax `.feature` files in the `test\acceptance` folder. PowerShell `.steps.ps1` files in the `step_definitions` sub-folder contain the implementation details for these acceptance tests.

  These tests are written in a [black box testing](https://en.wikipedia.org/wiki/Black-box_testing) style with limited direct access to internal infrastructure.

## Acceptance Test Documentation

* [Acceptance Test Structure](Acceptance-Test-Structure.md)

* [Tagging Acceptance Tests](Tagging-Acceptance-Tests.md)

* [Running Acceptance Tests](Running-Acceptance-Tests.md)

### Tooling Used

* [Docker](https://www.docker.com/)
* [Dredd](https://dredd.org/)
* [Pester](https://github.com/pester/Pester)
* [Selenium](https://www.seleniumhq.org/)
