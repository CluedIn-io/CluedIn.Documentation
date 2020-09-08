---
category: Crawler
title: Using Agents
---

Agents are the orchestrators of running integrations. Agents allow you to run crawlers in remote environments, typically on different machines, even in different physical environments. 

Agents are typically used for running hybrid environments of CluedIn where you may host CluedIn itself in the cloud, but need to run crawls on systems that live within an internal network of a business. 

The Agents are responsible for running scheduled crawls and the robustness of making sure that the crawlers can survive times where they crash. 

For running an Agent, you will need to register an Agent API key within the CluedIn datastore and then the Agents will need matching API keys in their configuration files on the remote machines. CluedIn will use Websockets to communicate between the Agents and the CluedIn Server. 

When deploying your Agents, they will need to have the Agent API key match one of the API Keys that are registered in the Agents Database within CluedIn. The API key must be associated with the Organization ID of the account that is running the Agent.

The simplest way to setup an agent is to remove the ServerComponent folder from CluedIn, leaving only the Agent folder. In container.config, you have to make sure that the URLs are correct (e.g. AgentServerUrl should have the value of the CluedIn's API endpoint).

For communication, Agents cannot receive incoming messages but rather uses a polling mechanism to talk with the CluedIn Server. In this way, other systems cannot instruct the Agents with a Job to run. The Agents will post data, logs and health statistics back to the CluedIn server so that CluedIn has knowledge of what is running within the Agents and any possible issues that could be happening. 
