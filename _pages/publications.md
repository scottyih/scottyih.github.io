---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

My work spans multi-agent systems, memory, automated research, retrieval-augmented language models, and question answering. For a curated introduction, see the [selected papers on my homepage]({{ base_path }}/#selected-papers).

You can also find my articles on [Google Scholar](https://scholar.google.com/citations?user=8rDNIMsAAAAJ) or [Semantic Scholar](https://www.semanticscholar.org/author/Wen-tau-Yih/144105277).

<nav class="publication-years" aria-label="Publication years">
  {% assign publication_years = site.publications | sort: "date" | reverse %}
  {% assign previous_year = "" %}
  {% for paper in publication_years %}
    {% assign year = paper.date | date: "%Y" %}
    {% if year != previous_year %}<a href="#year-{{ year }}">{{ year }}</a>{% endif %}
    {% assign previous_year = year %}
  {% endfor %}
</nav>

{% assign ordered_publications = site.publications | sort: "date" | reverse %}
{% assign previous_year = "" %}
{% for post in ordered_publications %}
  {% assign this_year = post.date | date: "%Y" %}
  {% if this_year != previous_year %}
    {% assign my_year = this_year %}
    {% include paper-list-year.html %}
  {% endif %}
  {% include paper-single.html %}
  {% assign previous_year = this_year %}
{% endfor %}


{% comment %}

{% for post in site.publications reversed %}
  {% include paper-single.html %}
{% endfor %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% endcomment %}



