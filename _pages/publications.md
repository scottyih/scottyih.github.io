---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

Will be updated soon. You can also find my articles on my <u><a href="https://scholar.google.com/citations?user=8rDNIMsAAAAJ">Google Scholar profile</a></u> or on my <u><a href="https://www.semanticscholar.org/author/Wen-tau-Yih/1725604">Semantic Scholar profile</a></u>.

{% for post in site.publications reversed %}
    {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
    {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}

    {% if forloop.first %}
        {% assign my_year = this_year %}
        {% include paper-list-year.html %}
    {% endif %}

    {% include paper-single.html %}

    {% if forloop.last %}
    {% else %}
      {% if this_year != next_year %}
        {% assign my_year = next_year %}
        {% include paper-list-year.html %}
      {% endif %}
    {% endif %}
{% endfor %}

{% comment %}

{% for post in site.publications reversed %}
  {% include paper-single.html %}
{% endfor %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% endcomment %}



