# Running Acceptance Tests

Acceptance tests are maintained within the `CluedIn.App` repository. When using the command line ensure that you are working within this repository.

## Pre-Requisites

In order to run acceptance tests in a local developer environment the following pre-requisites need to be met:

1. SSL certificates are available in the `tools\pki\certs` folder of the `CluedIn` repository.

   To generate SSL certificates required for the infrastructure run nthe following command as an Administrator and accept the certificate registrations when prompted to:

   ```PowerShell
   tools\pki\Create-Certificates.ps1
   ```

   The contents of the `tools\pki\certs` folder should be copied to the `CluedIn` repository when running with a local instance of the CluedIn server. From the `CluedIn.App` repository run the following command to copy the certificate files to the `CluedIn` repository folder:

   ```PowerShell
   copy .\tools\pki\certs\*.* ..\cluedin\tools\pki\certs\ -verbose -force
   ```

## Using Docker to run Acceptance Tests

Acceptance tests are executed by:

1. Follow instructions above to start the application
1. Run ```docker-compose -f .\docker-compose.tests.yml -f .\docker-compose.yml up -d```
1. You can follow the acceptance test results as they are executed: ```docker-compose -f .\docker-compose.tests.yml -f .\docker-compose.yml logs -f acceptance-tests```

## Running Tests on a Local Machine

You can also run the tests in bare-metal using a local browser (e.g. Chrome). Run the application normally (i.e. ```docker-compose up -d```)

1. In a console window run:

```Powershell
test/acceptance/Set-TestEnvironment.ps1
Invoke-Gherkin
```

You could also run the acceptance tests against the website running on bare metal (on port 5001):

1. Start the website (F5 on Visual Studio or ```dotnet run --project src/Cluedin.App```)
1. Run:

```Powershell
test/acceptance/Set-TestEnvironment.ps1 -TestUrl https://app.127.0.0.1.xip.io:5001
Invoke-Gherkin
```

## Running Tests Against Hosted Sites

To run the acceptance tests against a remotely hosted site set the `TestUrl` environment variable and invoke the test runner.

For example, the following commands run only the tests marked with a `Passive` impact tag against the `foobar` organization setup in CluedIn's `release23` test environment:

```PowerShell
.\test\acceptance\Set-TestEnvironment.ps1 -TestUrl https://foobar.release23.cluedin-test.online -Driver Chrome
Invoke-Gherkin -Tag Passive
```

The command below shows how to filter a test run by feature and scenario:

```PowerShell
Invoke-Gherkin .\test\acceptance\70.Homescreen.feature -ScenarioName 'Home menu navigation'
```

## Related Documentation

* [Acceptance Test Overview](Acceptance-Test.md)

* [Acceptance Test Structure](Acceptance-Test-Structure.md)

* [Tagging Acceptance Tests](Tagging-Acceptance-Tests.md)
