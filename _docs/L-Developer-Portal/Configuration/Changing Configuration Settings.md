Changing Configuration Settings

CluedIn provides configuration files that allow developers to modify the behaviour of CluedIn. The default configuration file that is used is called container.config and you can override the configuration using the computer name syntax of contain.<Your Computer Name>.config. This allows you to have different configuration files that you can have on your local developer machine so everyone is not always using the same configuration files. 

The Configuration file contains:

- Datastore Connection Strings
- Settings
- Feature Toggles
- Processing Pipeline Steps
- Global API Tokens
- Mail Settings

If you are deploying using the Kubernetes / Docker approach or are using this approach on your local developer machine, you will find that you can use a different mechanism to inject settings into your CluedIn configuration. 

Changing the settings in this file, will require you to reset the CluedIn component that you are running. 