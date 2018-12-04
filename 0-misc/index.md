# Misc

## Architecture

3 main services:

- [Application Services](./application-services.md)

Application services are non-domain specific APIs needed to have a UI up and running.

- Domain Services

Domain services are all the endpoints that creates the core of the CluedIn API.

Ideally the domain services should be a single GQL Endpoints.

- Auth Services

Authentication and Authorization services shared among the Application and Domain Services.

## Stack

**B-E**

- Micro services C# .NET

**F-E**

- SPA (react)

**Devops**

- Docker
- Kubernetes
- Helm
- Azure Devops

### Vendors

- Neo4j (graph db)
- Elastic Search (search)
- Log stash (logs)
- sql server (relational db)
- rabbitmq (queueing message)
- redis (cache)
- sentry (error reporting)



