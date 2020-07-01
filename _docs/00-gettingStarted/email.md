# TODO
* Replace with cluedin.ps1 env ?

---
category: Get Started
title: Configuring the Helm Chart
hideMenu: true
---

## Email configuration

The CluedIn application requires access to a SMTP server to send email. You can pass its access credentials in the following properties:

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