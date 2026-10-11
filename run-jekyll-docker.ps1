# powershell script to ensure this runs well on Windows 10
# source of information on how this was done was combined from the following resources:
# https://github.com/envygeeks/jekyll-docker
# https://tonyho.net/jekyll-docker-windows-and-0-0-0-0/
# https://jekyllrb.com/docs/configuration/options/
# note: can take up to 5 minutes to come up
# note: serve speed can be sped up by removing the --verbose flag
# note: mounts the folder this script is in, so it can be run from any directory
# note: --force_polling is required so livereload detects file changes
#       through the Windows Docker bind mount (native FS events don't
#       fire through the mount, so without polling edits don't rebuild)
# note: the bash commands are passed without carriage returns, because Git
#       checks this file out with CRLF line endings on Windows and bash
#       fails on them ("$'\r': command not found")
$bashCommands = @'
apt-get update &&
apt-get install -y --no-install-recommends nodejs npm &&
rm -rf /var/lib/apt/lists/* &&
gem install bundler -v 2.2.27 &&
bundle install &&
bundle exec jekyll serve --host 0.0.0.0 --livereload --force_polling --trace --verbose --config _config.yml,_config.docker.yml
'@ -replace "`r", ""

docker run --rm --name cluedin-docs `
  -e JEKYLL_ENV=docker `
  -p 4000:4000 -p 35729:35729 `
  -v "${PSScriptRoot}:/srv/jekyll" -w /srv/jekyll `
  ruby:3.3-bookworm `
  bash -lc $bashCommands
