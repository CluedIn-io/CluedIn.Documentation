---
layout: cluedin
nav_order: 9.6
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/snowflake-connector
title: Snowflake connector
last_modified: 2026-10-07
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to find the Snowflake connection details, configure key-pair authentication, and add a Snowflake export target in CluedIn.

This guide applies to the connector configuration that includes **Account Identifier**, **User**, and **Private Key (PEM)**. Older connector versions with username/password fields have a different configuration.

## Prerequisites

Before configuring the connector, make sure that you have:

- A Snowflake account accessible from your CluedIn environment.
- A destination database and schema, and a warehouse for executing export operations.
- A Snowflake user with key-pair authentication configured.
- A role granted to that user with access to the destination and the permissions needed by the export.
- OpenSSL installed on the computer where you will generate the keys.
- The Snowflake connector available in **Consume** > **Export Targets** in CluedIn.

Use a dedicated integration user and role. A Snowflake administrator should create or approve the user and grant the required access.

## Find your Snowflake connection details

Sign in to Snowsight, open your user menu, and select **Connect a tool to Snowflake**. The **Account Details** dialog provides connection settings. For the account identifier, use the organisation and account format, for example, `myorg-myaccount`. Enter the identifier only, without `https://` or `.snowflakecomputing.com`.

Alternatively, run the following in a Snowflake SQL worksheet:

```sql
SELECT
    CURRENT_ORGANIZATION_NAME() || '-' || CURRENT_ACCOUNT_NAME()
        AS ACCOUNT_IDENTIFIER,
    CURRENT_USER()      AS USER_NAME,
    CURRENT_ROLE()      AS ROLE_NAME,
    CURRENT_WAREHOUSE() AS WAREHOUSE_NAME,
    CURRENT_DATABASE() AS DATABASE_NAME,
    CURRENT_SCHEMA()   AS SCHEMA_NAME;
```

The results describe your current session. If you plan to use a separate integration user or role, enter its details in CluedIn instead. A null warehouse, database, or schema means that object has not been selected in the session.

Use the following commands to list objects visible to your current role. Replace the example database and schema names with your destination:

```sql
SHOW WAREHOUSES;
SHOW DATABASES;
SHOW SCHEMAS IN DATABASE CLUEDIN_DB;
SHOW TABLES IN SCHEMA CLUEDIN_DB.EXPORTS;
```

You can also locate the destination by expanding the database, schema, and table in Snowsight's database explorer.

For more information, see Snowflake's [connection settings guide](https://docs.snowflake.com/en/user-guide/gen-conn-config).

## Configure key-pair authentication

CluedIn holds the private key; Snowflake holds the matching public key assigned to the user. The private key is generated outside Snowflake and cannot be downloaded from Snowflake.

### Generate the keys

On a Mac, open **Terminal**. On Windows or Linux, use a terminal with OpenSSL installed. Run:

```bash
openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 aes-256-cbc -inform PEM -out cluedin_snowflake_key.p8
```

Choose and retain the encryption passphrase when prompted. Then generate the public key:

```bash
openssl rsa -in cluedin_snowflake_key.p8 -pubout -out cluedin_snowflake_key.pub
```

The `.p8` file contains the encrypted PKCS#8 private key. The `.pub` file contains the public key.

{:.important}
Keep the private key and passphrase secure. Do not paste them into tickets or commit them to source control.

### Assign the public key to the user

Open `cluedin_snowflake_key.pub`. Copy the key body without the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` lines, and remove line breaks.

Have an administrator with permission to modify the user's authentication methods run:

```sql
ALTER USER CLUEDIN_EXPORT
SET RSA_PUBLIC_KEY = 'PASTE_PUBLIC_KEY_BODY_HERE';
```

Replace `CLUEDIN_EXPORT` with the actual Snowflake user object name. Register the key against the user whose login name you will enter in CluedIn. Check for an existing registered key before replacing it, because other integrations may depend on it.

For current registration and rotation options, see Snowflake's [key-pair authentication guide](https://docs.snowflake.com/en/user-guide/key-pair-auth).

### Prepare the private key for CluedIn

Open `cluedin_snowflake_key.p8` and copy the entire file, including:

```text
-----BEGIN ENCRYPTED PRIVATE KEY-----
...
-----END ENCRYPTED PRIVATE KEY-----
```

Paste the complete contents into **Private Key (PEM)** in CluedIn. Enter the encryption passphrase in **Private Key Passphrase**. Do not enter a file path or your Snowflake password.

If your organisation supplies an unencrypted private key, include its `BEGIN PRIVATE KEY` and `END PRIVATE KEY` lines and leave the passphrase field blank.

## Configure the Snowflake connector

1. On the navigation pane, go to **Consume** > **Export Targets**, and select **Add Export Target**.

1. On the **Choose Target** tab, select the Snowflake target, and select **Next**.

1. On the **Configure** tab, complete the following fields.

| Field | What to enter |
|---|---|
| **Name** | A user-friendly label, for example, `Snowflake Customer Export`. This is a CluedIn label, not a Snowflake object. |
| **Account Identifier** | Your Snowflake account identifier, for example, `myorg-myaccount`. |
| **User** | The integration user's Snowflake login name. An email address is valid only if it is the user's login name. |
| **Private Key (PEM)** | The complete PEM private key, including its header, footer, and line breaks. |
| **Private Key Passphrase** | The passphrase used to encrypt the private key. Required only for an encrypted key. |
| **Database** | The destination database name, for example, `CLUEDIN_DB`. |
| **Schema** | The schema within that database, for example, `EXPORTS`. |
| **Warehouse** | The compute warehouse used for export operations, for example, `CLUEDIN_WH`. |
| **Role** | A role granted to the integration user that can perform the export. When blank, the user's default role is used. |
| **Table Name** | The target table name, for example, `CUSTOMERS`, within the configured database and schema. |
| **Output Format** | Select the required format from the options available in your connector version. This is configured in CluedIn. |
| **Export Schedule** | Select when CluedIn should export. The schedule uses UTC. This is configured in CluedIn. |

For example, the values `CLUEDIN_DB`, `EXPORTS`, and `CUSTOMERS` identify the destination `CLUEDIN_DB.EXPORTS.CUSTOMERS`.

{:.note}
Use the exact object names. Snowflake normally stores unquoted identifiers in uppercase; quoted identifiers can be case-sensitive.

1. Select **Test connection**.

1. When the connection test succeeds, select **Add**.

The export target is now available when configuring a [stream](/consume/streams). Configure the stream's records and output fields, then run a small sample export.

The connector configuration describes the target table as the table into which rows are merged. Before exporting, confirm the required target columns and whether your connector version creates the table automatically. If it requires an existing table, create one compatible with the stream output.

## Snowflake permissions

The integration role must have `USAGE` on the warehouse, database, and schema. For an existing destination table, grant the table privileges needed by the connector's operations.

The following is an example for an existing table. Have your Snowflake administrator adapt it to your export and replace the example names:

```sql
GRANT USAGE ON WAREHOUSE CLUEDIN_WH TO ROLE CLUEDIN_EXPORT_ROLE;
GRANT USAGE ON DATABASE CLUEDIN_DB TO ROLE CLUEDIN_EXPORT_ROLE;
GRANT USAGE ON SCHEMA CLUEDIN_DB.EXPORTS TO ROLE CLUEDIN_EXPORT_ROLE;

GRANT SELECT, INSERT, UPDATE ON TABLE CLUEDIN_DB.EXPORTS.CUSTOMERS
    TO ROLE CLUEDIN_EXPORT_ROLE;

GRANT ROLE CLUEDIN_EXPORT_ROLE TO USER CLUEDIN_EXPORT;
```

This example is not a complete permission set for every connector version. Additional privileges may be needed for table creation, staging objects, or delete operations. Scope additional access to the destination used by the export.

See Snowflake's [privilege reference](https://docs.snowflake.com/en/user-guide/security-access-control-privileges).

## Verify the export

A successful connection test does not prove that the complete export can write to the destination.

1. Export a small number of records through the configured stream.
1. Review the [stream logs](/consume/streams/stream-logs) for errors.
1. In Snowflake, query the destination:

   ```sql
   SELECT *
   FROM CLUEDIN_DB.EXPORTS.CUSTOMERS
   LIMIT 10;
   ```

1. Confirm that the expected records and columns are present before exporting the full dataset.

## Troubleshooting

| Issue | What to check |
|---|---|
| Authentication fails | Check the account identifier and login name. Confirm that the public key registered on that user matches the private key supplied to CluedIn. |
| Private key cannot be read | Paste the entire PEM file with actual line breaks. Confirm the passphrase for an encrypted key. |
| Role cannot be used | Confirm that the role is granted to the integration user. If the field is blank, check the user's default role. |
| Warehouse, database, schema, or table is unavailable | Check the object name and the selected role's privileges. An object may be hidden from a role that cannot access it. |
| Connection succeeds but export fails | Review stream logs for table column mismatches, missing write privileges, or permissions required for staging and table creation. |
| Connection is blocked | Check Snowflake network policies and connectivity from the CluedIn environment, including its outbound IP addresses. |
| Export runs at the wrong local time | Check the UTC schedule. For example, 00:00 UTC is 10:00 in Brisbane. |
