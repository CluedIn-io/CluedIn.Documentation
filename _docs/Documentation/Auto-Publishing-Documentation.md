## Auto Publishing Repository Documentation to Git Hub Pages

1. Create a '/docs' (*all lowercase*) folder under the root of your repository 
2. Add the following to your repositories `azure-pipelines.yml` to create a build artifact

```
resources:
  repositories:
  - repository: templates
    type: github
    name: CluedIn-io/AzurePipelines.Templates
    endpoint: 'CluedIn-io (2)'

steps:
 - template: documentation.publish.yml@templates
 ```


3. Go to [Azure Release Pipelines](https://dev.azure.com/CluedIn-io/CluedIn/_releaseDefinition?definitionId=14&_a=definition-pipeline) and add a new GitHub Artifact pointing to your Build pipeline, above
4. Click the 'lightning' symbol on your new Artifact and enable `Continuous Deployment Trigger`

