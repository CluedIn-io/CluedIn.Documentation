Crawler Validation Framework

While building new integrations for CluedIn, you will want to make sure that you are building your integrations correctly. The crawler validation framework will help guide a developer to produce a Clue that is of the highest readiness for processing. The validation framework will only run during Debug / Developer mode and will not run once deployed to production. 

The validation framework acts as a guide to warn a developer if they may have forgotten to do something important such as setting a Uri, setting a Name. It might be the case that you don't haave these properties (which is fine and normal) but it is also one of those pieces that is easy to forget - hence the framework. 

A developer can supress the validators at a Clue Producer level in the cases where you can confirm that you won't be able to produce what is expected for a Clue. 