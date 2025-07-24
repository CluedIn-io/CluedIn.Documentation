---
layout: cluedin
nav_order: 4
parent: Configuration
grand_parent: PaaS operations
permalink: {{ site.baseurl }}/deployment/infra-how-tos/configure-email
title: Email
tags: ["deployment", "kubernetes", "email"]
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Emails within CluedIn application are primarily used for inviting a user to the platform for management.
When single-sign on becomes enabled, the use of emails is not really required anymore.

In order to send emails, CluedIn must be configured with an SMTP server.
This can be a company owned one for your organization or a temporary one using a service such as MailTrap or Sendgrid, for example, which are useful for simple testing.

## Email configuration - local installation (Home)

Email configuration is simplified when running locally by using the `cluedin.ps1` helper script that comes part of the CluedIn Home repository.

You can configure any email settings as environment variables that will be passed into the application at runtime.

This is achieve by using the `env` command :

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

## Email configuration - Kubernetes

When using Kubernetes, the SMTP setting can be configured in the `values.yaml`. This can be done by setting the following properties:

```yaml
boostrap:
  email:
    host:
    port:
    user:
    password:
    senderName:
    senderDisplayName:
    fromAddress:
```

This will create a secret, storing the user and password information.  
Should you want to pass a secret already containing those details, you can create a secret with the keys:

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