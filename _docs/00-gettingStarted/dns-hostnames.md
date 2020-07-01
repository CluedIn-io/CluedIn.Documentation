# TODO
* This has changed so needs re-write
* Not sure these are configurable any more

---
category: Get Started
title: Configuring the Helm Chart
hideMenu: true
---

## Hostnames and addresses

CluedIn is a web a application, so users will access it from their browser. The main URL will take the form: 
 `https://<app-segment>.<prefix>.<hostname>`. 
 CluedIn is a multi-tenant application, so you can have different organizations/units in your company that can use CluedIn with total separation. So in order to use CluedIn you will need to create at least one *organization*. Each organization gets a different URL: `https://<organization>.<prefix>.<hostname>`. Since any number of organizations can be created from the application, the recommendation would be to map `*.<prefix>.<hostname>` to the public IP of the ingress of the cluster.

In addition to the actual web application, other  components need to be accessible from the outside, and therefore will be mapped to some URLs.

| component  | default url
|------------|--------------------------------------|
| api        | `https://<prefix>.<server-segment>.<hostname>`
| auth       | `https://<prefix>.<auth-segment>.<hostname>`
| public api | `https://<prefix>.<public-segment>.<hostname>`
| clean      | `https://<clean-segment>.<prefix>.<hostname>`
| webhooks   | `https://<prefix>.<webhook-segment>.<hostname>`

The `<prefix>` can be an empty string (i.e. no prefix) and you can define the value for each of the segments (app, server, auth, etc.). By default they are set to the name of those tokens without the word segment, e.g. the default value for the `<server-segment>` is `server`. All of these values can be adjusted changing the helm chart installation options.

```yaml
dns:
  prefix: # defaults to the release name, set to none to disable prefixes.
  hostname: # add the hostname suffix - i.e. my-org.com
  subdomains:
    app: 'app'
    api: 'server'
    public_api: 'public'
    auth: 'auth'
    clan: 'clean'
    webhook: 'webhook'
```