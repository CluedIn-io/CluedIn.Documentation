# Acceptance Test Structure

## User Interface

The scope for acceptance testing of the CluedIn user interface is defined in [GitHub Issue #981](https://github.com/CluedIn-io/CluedIn.Widget/issues/981).

The acceptance test release scenarios are listed below with links to the related test scripts:

1. App Root
    * [Single Page Application](../test/acceptance/05.SinglePageApplication.feature)
2. Login
    * [Login](../test/acceptance/10.Login.feature)
    * [Forgotten Password](../test/acceptance/20.ForgottenPassword.feature)
3. Homescreen
    * [Homescreen](../test/acceptance/70.Homescreen.feature)
4. Integration
    * [Integrations](../test/acceptance/75.Integrations.feature)
    * [Integration Permissions](../test/acceptance/85.IntegrationPermissions.feature)
5. Search
    * [Simple Search](../test/acceptance/80.SimpleSearch.feature)
6. Entity
    * [Followed Entities](../test/acceptance/81.FollowedEntities.feature)
7. Users
    * [Users](../test/acceptance/82.Users.feature)
    * [Invite New User](../test/acceptance/30.InviteNewUser.feature)
    * [Manage Invites](../test/acceptance/60.ManageInvites.feature)
8. Data Governance
    * [Data Governance](../test/acceptance/84.DataGovernance.feature)
9. Developer
    * [Developer](../test/acceptance/85.Developer.feature)
10. Settings
    * [Settings](../test/acceptance/86.Settings.feature)
11. Logout
    * [Login](../test/acceptance/10.Login.feature)
12. Follow
    * [Followed Entities](../test/acceptance/81.FollowedEntities.feature)

The following acceptance test scripts are currently unmapped to GitHub release scenario definitions:

* [Single Page Application](../test/acceptance/05.SinglePageApplication.feature)
* [Domain Signup](../test/acceptance/40.DomainSignup.feature)
* [Change Password](../test/acceptance/50.ChangePassword.feature)

## Customer Setup

The following tests cover the tasks of setting CluedIn up for a new customer:

* [Create Organization](../test/acceptance/07.CreateOrganization.feature)

## API

Acceptance tests covering the application API are provided in:

* [API Dashboard](../test/acceptance/90.Api.Dashboard.feature)
* [API Schema](../test/acceptance/91.Api.Schema.feature)

## Non-Functional Requirements

Non-functional acceptance tests scripts are provided for:

* [Security](../test/acceptance/01.Security.feature)
* [Logging](../test/acceptance/95.Logging.feature)

## Related Documentation

* [Acceptance Test Overview](Acceptance-Test.md)

* [Running Acceptance Tests](Running-Acceptance-Tests.md)

* [Tagging Acceptance Tests](Tagging-Acceptance-Tests.md)
