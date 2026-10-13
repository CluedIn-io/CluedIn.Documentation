---
title: Configuration
url: https://documentation.cluedin.net/operate/configuration
content_type: landing
section: Deploy & operate
---

# Configuration


## In this section

- [Connect to CluedIn cluster](https://documentation.cluedin.net/operate/configuration/connect-to-cluedin.md) (how-to): Azure Cloud Shell provides an effective environment and the tools you need to interact with your AKS cluster without significant configuration or effort.
- [SSO](https://documentation.cluedin.net/operate/configuration/configure-sso.md) (how-to): In this article, you will learn how to configure single sign-on (SSO) for CluedIn using Microsoft Entra group-managed role membership.
- [Advanced network configuration](https://documentation.cluedin.net/operate/configuration/advanced-network.md) (how-to): In this article, you will learn about advanced network configuration options that are available to you during CluedIn installation.
- [Email](https://documentation.cluedin.net/operate/configuration/configure-email.md) (how-to): Emails within CluedIn application are primarily used for inviting a user to the platform for management.
- [Logging](https://documentation.cluedin.net/operate/configuration/configure-logging.md) (how-to): In this article, you will get an overview of the logging options and learn how to configure the logging level that you need.
- [TLS certificates](https://documentation.cluedin.net/operate/configuration/configure-certificates.md) (how-to): The CluedIn front-end application uses Transport Layer Security (TLS) to encrypt access to the application over the network using HTTPS.
- [DNS](https://documentation.cluedin.net/operate/configuration/configure-dns.md) (how-to): As part of the CluedIn configuration, a base URL is used to make the application easily accessible by your browser.
- [PVC](https://documentation.cluedin.net/operate/configuration/persistence.md) (how-to): By default, all deployments that store state (sqlserver, elasticsearch, rabbitmq, redis, openrefine) are defined with some storage in order to persist the state.
- [Alerts](https://documentation.cluedin.net/operate/configuration/configure-alerts.md) (how-to): By default, CluedIn contains built-in alerts that are sent to our support team.
- [Firewall](https://documentation.cluedin.net/operate/configuration/configure-firewall.md) (how-to): Your Azure Firewall should cover the following:
- [SQL Server](https://documentation.cluedin.net/operate/configuration/sql.md) (how-to): By default, SQL Server is deployed within the cluster.
- [Modify web response headers](https://documentation.cluedin.net/operate/configuration/modify-response-headers.md) (how-to): By default, CluedIn is configured with web security in mind and out of the box is quite secure.
- [Create dedicated stream processing pod](https://documentation.cluedin.net/operate/configuration/dedicated-stream-processing-pod.md) (how-to): In this article, you'll find instructions for creating a dedicated pod that only processes streams.
- [Private Endpoints](https://documentation.cluedin.net/operate/configuration/private-endpoint.md) (how-to): CluedIn supports private endpoint connections via an internal load balancer.
- [Sync certificates and secrets from AKV to AKS](https://documentation.cluedin.net/operate/configuration/sync-aks-to-akv.md) (how-to): In this article, we will guide you through connecting your CluedIn instance to use the existing Azure Key Vault (AKV) to synchronize secrets and certificates to your Kubernetes cluster.
- [Sync configuration between environments](https://documentation.cluedin.net/operate/configuration/sync-configuration-between-environments.md) (how-to): This document covers the process for migrating CluedIn configuration from one environment to another environment.
- [Configuration import and export](https://documentation.cluedin.net/operate/configuration/configuration-import-export.md) (how-to): The Configuration Import / Export feature lets you move CluedIn configuration between environments directly from the user interface.
- [CI/CD for CluedIn configuration with GitHub Actions](https://documentation.cluedin.net/operate/configuration/configuration-cicd.md) (how-to): This article explains how to use GitHub Actions and CluedIn.Product.Toolkit to capture configuration from a CluedIn development environment and promote the reviewed configuration to test and production environments.

Up: [Deploy & operate](https://documentation.cluedin.net/operate.md)
