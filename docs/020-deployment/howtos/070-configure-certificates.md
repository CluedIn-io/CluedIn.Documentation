---
layout: default
nav_order: 1
parent: How-to guides
grand_parent: Installation
permalink: /deployment/infra-how-tos/configure-certificates
title: Configure certificates
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

The CluedIn front-end application uses **Transport Layer Security (TLS)** to encrypt access to the application over the network using HTTPS. CluedIn uses the Automated Certificate Management Environment (ACME) protocol and the public  Let's Encrypt certificate authority to issue certificates.

While there are no specific requirements regarding the issuer and source of your certificates and keys, it is recommended that all TLS certificates and keys meet your organization's requirements and comply with any security and compliance policies and regional laws.

In this article, you will learn how to create your own certificates and keys and update your server configuration with the newly generated certificates and keys. Also, you will learn about alternative certificate providers.

**Prerequisites**

- You should be comfortable working in either PowerShell or bash terminal via Azure Cloud Shell.
- You should be connected to your AKS cluster.

    See [Connect to CluedIn cluster](/deployment/infra-how-tos/connect-to-cluedin) for detailed instructions.

- Your Helm repository is set up.

If you have any questions, you can request CluedIn support by sending an email to <a href="mailto:support@cluedin.com">support@cluedin.com</a> (or reach out to your delivery manager if you have a committed deal).

# Create your own certificates and keys

If you want to use a Subject Alternative Name (SAN) or wildcard certificate for you domain, create your own certificates and keys.

**To create certificates and keys**

1. From a suitable provider, obtain the following files: **TLS certificate**, **TLS private key (without password)**, and **Certificate authority's public certificate**.

    The TLS certificates and keys must contain the DNS names for the CluedIn services as described in [Configure DNS](/deployment/infra-how-tos/configure-dns).

2. After you obtain the required files, convert the content of each file to base64 string using the `output.txt` command. For example: `bas64 /path/to/file > output.txt`
3. Add the strings to your **values.yaml** file under the **Platform** section as shown in the example below.
```yaml
platform:
  extraCertificateSecrets:
    cluedin-frontend-crt:
      tlsKey: LS0tLS1CRUdJTiB0tLS0tCk1JSUZuekNDQTRlZ0F3SUJBZ0lVTjU1RW95TkVPK3=
      tlsCrt: S0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZuekNDQTRlZ0F3SUJBZ=
      caCrt:  LS0tLS1CRUdJTiB0tLS0tCk1JSUZuekNDQTRlZ0F3SUJBZ0lVTjU1RW95TkVPK3=
```
4. Save the file.

# Update your server configuration via Helm

After you added the certificates and keys to your **values.yaml** file, you need to update the server configuration with your new TLS certificates and keys.

**To update the server configuration via Helm**

1. Get the current TLS values by running the following command:
```
helm get values cluedin-platform -n cluedin -o yaml > Cluster-Current-values.yaml
```
This command downloads the current cluster configuration that you can use to update your server configuration.

2. Open the file in the text editor of your choice (for example, nano).
```
nano Cluster-Current-values.yaml
```

3. Add the section with base64 encoded values for the keys and secrets.
```yaml
platform:
  extraCertificateSecrets:
    cluedin-frontend-crt:
      tlsKey: LS0tLS1CRUdJTiB0tLS0tCk1JSUZuekNDQTRlZ0F3SUJBZ0lVTjU1RW95TkVPK3=
      tlsCrt: S0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZuekNDQTRlZ0F3SUJBZ=
      caCrt:  LS0tLS1CRUdJTiB0tLS0tCk1JSUZuekNDQTRlZ0F3SUJBZ0lVTjU1RW95TkVPK3= # Optional. Used for self-signed or missing CA certificates. Needs global.ingress.tls.hasClusterCA set to 'true' to be used.
```

4. Remove the following section of configuration.
```yaml
  issuer:
    configuration:
      acme:
        email: aba@cluedin.com
        privateKeySecretRef:
          name: letsencrypt-production
        server: https://acme-v02.api.letsencrypt.org/directory
        solvers:
        - http01:
            ingress:
              ingressTemplate:
                metadata:
                  annotations:
                    kubernetes.io/ingress.class: haproxy
    isWildcard: false
```
**Note:** We recommend that you remove Let's Encrypt issuer because you are configuring the system to use your own certificates and keys.

5. Update the ingress controller to use the new certificate:
```yaml
global:
  ingress:
    tls:
      hasClusterCA: true # Only set to 'true' if the CA certificate is not publicly trusted.
      secretName: cluedin-frontend-crt # Must match name of secret in platform.extraCertificateSecrets
```

6. Finally, update the hostname field to match the DNS for ingress.
```yaml
global:
  dns:
    hostname: mydomain.com # By default will be sslip.io
```

7. Save the file.

8. Post the new configuration to your cluster by running the following command:
```
helm upgrade -i cluedin-platform cluedin/cluedin-platform  -n cluedin --create-namespace  --values Cluster-Current-values.yaml --set application.system.runDatabaseJobsOnUpgrade=false
```
After a short time, you'll see the confirmation of your update in the console. CluedIn is now configured to use your new TLS certificate and keys.

# Alternative certificate providers

If you can't obtain a certificate from a commercial certificate authority or from your internal public key infrastructure (PKI) service, you can use other methods to generate certificates. For example, you can generate certificates via [Let's Encrypt](#lets-encrypt) or you can generate [self-signed certificates](#self-signed-certificates).

While these methods provide the same level of encryption as the commercial and PKI issued certificates, they don't provide the same level of validation.

Make sure that any certificates and keys that you use meet your organization's security policies.

## Let's Encrypt

Let's Encrypt provides the ability to generate the required certificates and keys to be used for free. These certificates are issued by a widely accepted certificate authority managed by  [Internet Security Research Group](https://www.abetterinternet.org/). Certificates from Let's Encrypt provide a low-cost, low-maintenance alternative to commercial or internal PKI providers.

For more information about Let's Encrypt, visit [their website](https://letsencrypt.org/).

## Self-signed certificates

Self-signed certificates should only be used in non-production environments where organizational policies approve this approach.

The following procedure shows how to create a self-signed certificate using OpenSSL. In the procedure, the certificate is created for `mycompany.com` and the expiration period is 10 years.

**To create self-signed certificate**

1. Generate the certificate:
```
openssl req -x509 -newkey rsa:4096 -keyout domain.key -out domain.crt -sha256 -days 3650 -nodes -subj "/CN=mycompany.com"
```

1. Verify the certificate:
```
openssl x509 -text -noout -in domain.crt
```

1. Convert the certificate into the .pfx format:
```
openssl pkcs12 -inkey domain.key -in domain.crt -export -out domain.pfx
```

