---
layout: default
nav_order: 3
parent: Kubernetes
grand_parent: Deployment
permalink: /deployment/kubernetes/create-organization
title: Create an Organization
tags: ["deployment", "kubernetes", "organization"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}
### Organization

CluedIn can support [multitenancy](../../administration/multitenancy) (disabled by default).

As such, the first thing you need to do for using CluedIn once installed is to create an organization.

### Pre-requirement

- A configured SMTP

By default, CluedIn is not shipping with any SMTP servers. You need to setup it before creating your organization.

Emails are transactional emails. You won't receive marketing email. They are emails to inform you of some important actions that was taken by your users using your CluedIn installation and/or emails used for security check (signup, change password, invitation...)

Visit [How to configure SMTP](./email)

### Create organization through the UI

Visit our sign up URL: `https://app.[cluedin-domain]/signup`

> Organization name MUST be longer than 2 letters

> Some name are being reserved by CluedIn. For privacy reasons, this list is kept private. If you have trouble entering your name, contact CluedIn support.

1. Enter your email 
2. You will receive an email with a link to create your user, click on that click
3. Follow the process (pick org name, username, password, accept Terms)
4. You will be redirect to the login page, use the credentials defined in the step above

### Create organization with a script

Execute the script [`./createOrg.ps1`](https://github.com/CluedIn-io/Cluedin-Docker-Local-Deployment/blob/master/bootstrap/Create-Organization.ps1) with the appropriate parameters.