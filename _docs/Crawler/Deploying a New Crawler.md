---
category: Crawler
title: Deploying a New Crawler
---

You can deploy new crawlers in two main ways:

1: Moving files into the ServerComponent directory and running the respective commands to inject the required data into the Relational Store. 

2: Use Docker to layer your crawler on top of the base CluedIn instance. 

For the first option, there are 3 main components that will need to be deployed:

1: *.dll files for each of the 4 projects of a Crawler. (You may choose to also take the *.pdb files so that you can debug)

2: You will need to run the provider.sql file in your Provider project as to instruct CluedIn that there is a new provider that is available. (Make sure the "Active" flag is set to true so that your integration is now available to add).

3: You will need to deploy your additional files for the web application e.g. Logo and some user interface mappings. 

Note: You will need to reboot the CluedIn host to properly pick up these changes. 

The second (and recommended) approach is to create a Docker container out of your crawler and then to change your Docker Compose file to reference your new Crawler. This will handle the entire deployment process for you and will even reboot the CluedIn host for you. This approach is recommended as it will also help to roll this new Crawler out to test and production environments with full capabilities of roll back and uninterrupted deployments. 