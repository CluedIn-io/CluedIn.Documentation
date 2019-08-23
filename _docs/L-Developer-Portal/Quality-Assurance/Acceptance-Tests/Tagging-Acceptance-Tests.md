# Tagging Acceptance Tests

Tags specified in Pester acceptance scripts are used to both indicate test dependencies and offer a means to control which tests execute.

> A tag allows a developer to organize their tests based on different criteria and execute those tests accordingly. Tags allow a developer to manage large test suites that may take hours to run by only executing certain tests matching certain tags.

## Tag Categories

Tags used in the acceptance tests can be categorized as follows:

* Tags that show the impact on the target environment of running the test

* Tags that document test dependencies and requirements

* Tags that document actions performed when running the test

* Tags that are solely used to filter which tests are executed in a particular run.

The list of tags for each of these categories are documented below in the following sections.

### Test Impact Tags

Tags can be used to indicate the impact of an acceptance test.

The following tags are recommended:

* _@Passive_

  The test performs read-only interactions with the target environment.

  This tag is optional.

* _@Safe_

  The test performs updates on data in the target environment that can be considered non-destructive.

  For example, a test that adds and then removes an integration component on a shared target environment should be marked with the `@Safe` tag.

* _@Active_

  The test performs updates on data in the target environment that can be considered destructive.

  For example, a test that changed a user's UI `Settings` on a shared target environment should be marked with the `@Active` tag.

__Note:__ Care should be taken to not run tests marked with a `@Active` tag against shared test environments.

### Tags Indicating Test Dependencies

The following tags can be used to specify pre-requisites for an acceptance test:

<!-- * _@Dredd_

  Test uses the `Dredd` command-line tool for validating API description document against a running backend instance of the application API.

  Not implemented -->

* _@Fullstack_

  Test requires the full CluedIn application stack to be running and available

* _@Selenium_

  Test utilises Selenium browser automation

* _@WithData_

  Test requires CluedIn application stack containing data.

### Tags Indication Test Actions

Actions performed by tests can be categorized with the following tags:

* _@Email_

  Test causes e-mail to be sent.

### Test Execution Control Tags

* _@Api_

  Selects tests validating the application API.

* _@CuttingConcerns_

  Select tests that should be executed after other acceptance tests have run.

* _@Logging_

  Selects tests validating the application logs.

* _@Security_

  Selects tests checking the security concerns of the application and it's users.

## Related Documentation

* [Acceptance Test Overview](Acceptance-Test.md)

* [Acceptance Test Structure](Acceptance-Test-Structure.md)

* [Running Acceptance Tests](Running-Acceptance-Tests.md)

* [Using Tags In PowerShell Pester For Unit Testing](https://blog.ipswitch.com/how-to-use-tags-in-a-powershell-pester-test)
