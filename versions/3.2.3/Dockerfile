FROM jekyll/jekyll:pages

COPY Gemfile* /srv/jekyll/

WORKDIR /srv/jekyll

RUN apk update && \
	apk add ruby-dev gcc make curl build-base libc-dev libffi-dev zlib-dev libxml2-dev libgcrypt-dev libxslt-dev python

RUN chmod a+w Gemfile.lock && \
	bundle config build.nokogiri --use-system-libraries && \
	bundle install

EXPOSE 4000
