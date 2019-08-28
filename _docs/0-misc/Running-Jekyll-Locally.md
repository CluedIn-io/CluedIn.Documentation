---
category: Misc
---

# Running Jekyll Locally

## What is Jekyll

Kekyll is a simple engine that allows you to transform your plain text into static websites and blogs.

## Downloading and running container

To download Jekyll Docker image use the following:

```
docker pull jekyll/jekyll
```

To run the container mounted to a specific location on local file-system, ie, where you documentation files are located:

```
docker run --mount type=bind,source=C:/myfolder,target=/srv/jekyll -p 4000:4000 -it jekyll/jekyll:builder bash
```

*Replacing c:/myfolder as appropriate. If running successfully, you'll be presented with a `bash` command-line

## Adding documentation and testing locally

Within the `c:/myfolder` above you can now add .md, .html and images files. To compile these, from hte `bash` command-line, use the following to parse and compile the files:

```
jekyll build
```

To run and test them under the server use the following:

```
jekyll serve
```

You should now be able to browser the generated files navigating to [http://localhost:4000](http://localhost:4000) in a browser

## References

[Jekyll](https://jekyllrb.com/) 

[Jekyll Docker Container](https://hub.docker.com/r/jekyll/jekyll/) 
