---
layout: default
nav_order: 1
parent: CluedIn
grand_parent: Deployment
permalink: /deployment/cluedin/email
title: Email
tags: ["deployment", "kubernetes", "email"]
last_modified: "2021-09-20"
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In order to send emails, CluedIn must be configured with an SMTP server.
This can be a company owned one for your organization or a temporary one using a service such as MailTrap or Sendgrid, for example, which are useful for simple testing.

## Email Configuration - Docker/Local Machine

Email configuration is simplified when running localy by using the `cluedin.ps1` helper script.

You can configure any email settings as environment variables that will be passed into the application at runtime.

This is acheive by using the `env` command :

```bash
./cluedin.ps1 env -set [NAME]=[VALUE]
```

The possible values for configuring email in CluedIn are:

```
CLUEDIN_EMAIL_HOST             (default: <blank>)
CLUEDIN_EMAIL_PASS             (default: <blank>)
CLUEDIN_EMAIL_PORT             (default: 587)
CLUEDIN_EMAIL_SENDER           (default: noreply@cluedin.com)
CLUEDIN_EMAIL_USER             (default: <blank>)   
```

## Email Configuration - Kubernetes

WHen using Kubernetes the SMTP setting can be configured in the `values.yaml`. This can be done by setting the following properties:

```yaml
email:
  host:
  port:
  user:
  password:
  senderName:
  senderDisplayName:
```

This will create a secret storing the user and password information. Should you want to pass a secret already containing those details, you can create a secret with the keys:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: <my-email-secret>
type: Opaque
data:
  EmailUserName: 
  EmailPassword: 
```

And pass the name of the secret in the property

```yaml
email:
    secretRef: <my-email-secret>
```

Passing a secret in this way will override the use of explicit user/password properties.