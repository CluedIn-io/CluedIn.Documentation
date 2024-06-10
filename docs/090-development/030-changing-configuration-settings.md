---
layout: cluedin
title: Changing Configuration Settings
parent: Development
nav_order: 030
has_children: false
permalink: /development/changing-configuration-settings
tags: ["development","configuration"]
published: false
---

CluedIn provides configuration files that allow developers to modify the behaviour of CluedIn. The default configuration file that is used is called container.config and you can override the configuration using the computer name syntax of container.<Your Computer Name>.config. This allows you to have different configuration files that you can have on your local developer machine so everyone is not always using the same configuration files. You can also use this to manage configuration on different hardware when you are not utilising the Kubernetes deployment model of CluedIn.

To retrieve the name of your computer you can open a terminal and type "hostname". This will work across all operating systems. 

The Configuration file contains:

- Datastore Connection Strings
- Settings
- Feature Toggles
- Processing Pipeline Steps
- Global API Tokens
- Mail Settings

If you are deploying using the Kubernetes / Docker approach or are using this approach on your local developer machine, you will find that you can use a different mechanism to inject settings into your CluedIn configuration. For this we will use the Docker YAML files to be able to set the settings within the underlying container.config files. 

Changing the settings in this file, will require you to reset the CluedIn component that you are running. 

If you are wanting to add your own configuration when you are making extensions to the platform then we also allow you to do this. The recommended approach is that you will need to add your lines in the configuration like: 

```xml
 <add key="Group.Key"  value="true" xdt:Locator="Condition(@key='Group.Key')" xdt:Transform="Replace" />
```

If you are adding your own configuration, it may be that you will also need to add this to the Docker YAML files. 

For documentation on describing the individual configuration settings, please install CluedIn and view the container.config file directly for inline comments. 