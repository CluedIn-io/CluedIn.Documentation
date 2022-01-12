# Documentation Repo Starting Point

Please have a read of the DevOps Wiki [here](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/168/Documentation)

## Introduction
We use jekyll as the templating for the documentation. You can read more about that here:

* https://idratherbewriting.com/documentation-theme-jekyll/
* https://kramdown.gettalong.org/

The documentation is published here:

* https://documentation.cluedin.net/

## Updating the Documentation
Please discuss on [#docs](https://cluedin.slack.com/archives/C028ZU4MUU8) on our slack. All changes to be done as pull requests with at least one reviewer (Rudi or Roman for example).

## Markdown QuickRef

* https://kramdown.gettalong.org/quickref.html

## View the Documentation Locally From Source
### Running The Docker Container
#### Windows Users
Run `run-jekyll-docker.ps1` script 

**note**: it can take upto 5 minutes to come up

#### Everyone Else
Run `docker compose`
#### View the Documentation

* open http://localhost:4000/

## Other Useful Tasks
### Check for Broken Links
`jekyll build ; htmlproofer --allow_hash_href --empty_alt_ignore --assume_extension --disable_external ./_site &> links.log`
