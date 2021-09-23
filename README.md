For Windows Users:
Run run-jekyll-docker.ps1 script (can take upto 5 minutes to come up)
Then open http://localhost:4000/

To check for broken links:
`jekyll build ; htmlproofer --allow_hash_href --empty_alt_ignore --assume_extension --disable_external ./_site &> links.log`