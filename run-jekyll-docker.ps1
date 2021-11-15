# powershell script to ensure this runs well on Windows 10
# source of information on how this was done was combined from the following resources:
# https://github.com/envygeeks/jekyll-docker
# https://tonyho.net/jekyll-docker-windows-and-0-0-0-0/
# https://jekyllrb.com/docs/configuration/options/
# note: can take up to 5 minutes to come up
# note: serve speed can be sped up by removing the --verbose flag
docker run --name CluedIn.Documentation --rm -e "JEKYLL_ENV=docker" --volume="${PWD}:/srv/jekyll" --publish 4000:4000 --publish 35729:35729 jekyll/jekyll bash -c "gem install bundler:2.2.27 && jekyll serve -w --livereload --incremental --force_polling --config _config.yml,_config.docker.yml"