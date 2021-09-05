
To check for broken links:
`jekyll build ; htmlproofer --allow_hash_href --empty_alt_ignore --assume_extension --disable_external ./_site &> links.log`