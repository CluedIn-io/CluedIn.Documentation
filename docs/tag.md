---
layout: default
title:
has_children: false
permalink: /tag
nav_exclude: true
sitemap: false
---

{% assign rawtags = "" %}
{% for post in site.pages %}
{% assign ttags = post.tags | join:'|' | append:'|' %}
{% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% assign tags = "" %}

{% for tag in rawtags %}
{% if tag != "" %}
{% if tags == "" %}
{% assign tags = tag | split:'|' %}
{% else %}
{% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
{% endif %}
{% endif %}
{% endfor %}

{% assign distinct_tags = tags | uniq %}

{% assign tag_groups = tags | group_by_exp: "item", "item" %}

{% assign sorted_tag_groups = tag_groups | sort_natural: "name" %}

{% assign biggest_tag = tag_groups | sort: "count" | last %}

{% for tag_group in sorted_tag_groups %}
<h3 data-tag="{{ tag_group.name }}" style="display:none;">Tag: {{ tag_group.name }}</h3>
<ul data-tag="{{ tag_group.name }}" style="display:none;">
    {% for page in site.pages %}
    {% if page.tags contains tag_group.name %}
    <li><a href="./{{ page.permalink }}">{{ page.title }}</a></li>{% endif %}{% endfor %}
</ul>
{% endfor %}

<script>
    $(function() {
        const tag = window.location.hash.replace('#', '');
        $('#main-content > h1:nth-child(1)').remove();
        $(`[data-tag='${tag}']`).show();
    });
</script>
