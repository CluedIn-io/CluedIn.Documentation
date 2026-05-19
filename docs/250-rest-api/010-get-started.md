---
layout: cluedin
title: Get started
parent: REST API
permalink: /rest-api/get-started
nav_order: 10
tags: ["api", "rest api"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This page explains how to connect to the CluedIn REST API: base URLs, authentication, and the conventions that requests and responses follow. For the full list of endpoints, see the [API reference](/rest-api/api-reference).

## Base URL

The API is served from your CluedIn environment under the `/api` path:

```
https://<organization>.<domain>/api
```

Replace `<organization>.<domain>` with the host of your own CluedIn environment—for example, `https://acme.cluedin.com/api`.

All requests must use HTTPS.

## Versioning

Most endpoints are available both unversioned and with an explicit version prefix:

```
https://<organization>.<domain>/api/accesscontrolpolicies
https://<organization>.<domain>/api/v1/accesscontrolpolicies
```

A small number of endpoints offer additional versions (for example, `/api/v2/search/suggest` and `/api/v3/search/suggest`).

{:.important}
For stability, prefer the explicit versioned path (`/api/v1/...`). Each endpoint's exact path and available versions are shown in the [API reference](/rest-api/api-reference).

## Authentication

The API uses **bearer token** authentication. Every request must include an `Authorization` header with a valid CluedIn API token:

```
Authorization: Bearer <your-api-token>
```

Include the word `Bearer`, followed by a single space, before the token value.

You generate API tokens in the CluedIn UI under **Administration** > **API Tokens**. For step-by-step instructions, see [Generate an API token](/administration/api-token).

{:.important}
Treat API tokens as secrets. Store them in a secure location such as a password vault, never commit them to version control, and revoke them when they are no longer needed.

### Permissions

Many endpoints require specific permissions in addition to a valid token. The required policy is shown in each endpoint's summary in the API reference (for example, `Auth policies: RACI:management.accesscontrol`). Make sure the token has been granted the corresponding scope; otherwise the request is rejected with `403 Forbidden`.

## Request and response format

- Send request bodies as JSON with the `Content-Type: application/json` header.
- Set `Accept: application/json` to receive JSON responses.
- Responses are returned as JSON. Some endpoints also support `text/json` and `text/plain`.

| Header | Value | When to send |
|---|---|---|
| `Authorization` | `Bearer <your-api-token>` | Every request. |
| `Content-Type` | `application/json` | Requests that include a body (`POST`, `PUT`, `PATCH`). |
| `Accept` | `application/json` | Recommended on every request. |

## Collection parameters

Endpoints that return collections commonly support the following query parameters for paging and sorting. The exact parameters and filters available for a given endpoint are listed in the [API reference](/rest-api/api-reference).

| Parameter | Type | Description |
|---|---|---|
| `page` | integer | Zero-based page index. Defaults to `0`. |
| `take` | integer | Number of items to return per page. Defaults to `20`. |
| `orderBy` | string | Name of the field to sort by. |
| `orderAsc` | boolean | Sort direction. Defaults to `true` (ascending). |

## Status codes

The API uses standard HTTP status codes.

| Code | Meaning |
|---|---|
| `200 OK` | The request succeeded. |
| `201 Created` | The resource was created successfully. |
| `400 Bad Request` | The request was malformed or failed validation. |
| `401 Unauthorized` | The token is missing, invalid, or expired. |
| `403 Forbidden` | The token is valid but lacks the required permission. |
| `404 Not Found` | The requested resource does not exist. |
| `409 Conflict` | The request conflicts with the current state of the resource. |
| `500 Internal Server Error` | An unexpected error occurred on the server. |

## Examples

The examples below use `/api/v1` paths. Set the `CLUEDIN_API_TOKEN` environment variable to your token before running them.

### Check connectivity

`GET /api/v1/status` reports whether the environment is reachable.

```bash
curl "https://<organization>.<domain>/api/v1/status" \
  -H "Accept: application/json"
```

### Authenticated GET request

The following request retrieves vocabulary keys.

```bash
curl "https://<organization>.<domain>/api/v1/vocabs/keys" \
  -H "Authorization: Bearer $CLUEDIN_API_TOKEN" \
  -H "Accept: application/json"
```

The same request in PowerShell:

```powershell
$headers = @{
    Authorization = "Bearer $env:CLUEDIN_API_TOKEN"
    Accept        = "application/json"
}
Invoke-RestMethod -Uri "https://<organization>.<domain>/api/v1/vocabs/keys" -Headers $headers
```

### Request with a JSON body

`POST`, `PUT`, and `PATCH` requests send a JSON body and must include the `Content-Type` header.

```bash
curl -X POST "https://<organization>.<domain>/api/v1/<resource>" \
  -H "Authorization: Bearer $CLUEDIN_API_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{ "name": "Example" }'
```

Refer to the [API reference](/rest-api/api-reference) for the exact request body schema of each endpoint.
