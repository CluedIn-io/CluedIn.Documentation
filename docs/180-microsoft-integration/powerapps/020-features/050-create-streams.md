---
layout: default
nav_order: 50
parent: Features
grand_parent: PowerApps Integration
permalink: /microsoft-integration/powerapps/features/create-streams
title: Create Streams
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

This feature will allow you to automate the creation of Export Targets and Streams
![Create CluedIn Streams](../images/create-stream-setting.png)
#### Export Targets
- Export Target will be created automatically using the same credentials from Organization Settings
![CluedIn Export Target](../images/create-export-target.png)
#### Streams
- The creation of a stream will depend on the values of Sync EntityTypes and Sync Dataverse Tables values.
- Once the execution of the Job is done, from the sample values above, you can expect 2 streams to be created, which is for the '**cluedin_dog**' and '**crc12_customer**' table.
![CluedIn Streams](../images/cluedin-stream.png)
- Each stream will have a certain configuration filtered by EntityType
![CluedIn Stream Configuration](../images/cluedin-stream-configuration.png)
- It will automatically assign the same export target that was created from the Dataverse connector. Incoming and Outgoing Edges are set to be exported. All the properties associated with it have been automatically added too.
![CluedIn Stream Export Target Configuration](../images/cluedin-stream-export-target-configuration.png)
#### Notifications
- 2 notifications can be expected in this job
  1. Stream Creation
  2. Updating the property mappings
- ![CluedIn Streams Notifications](../images/cluedin-stream-notification.png)