---
layout: default
title: papers
permalink: /papers/
---

<h1 class="text-2xl font-normal lowercase tracking-tight mb-8">papers</h1>

{% assign sorted = site.digests | sort: 'date' | reverse %}
{% for digest in sorted %}
  {% for paper in digest.papers %}
  <a href="{{ digest.url | relative_url }}" class="block py-4 border-b border-black/10 first:pt-0 hover:text-bolt transition-colors">
    <p class="text-xs text-black/40 mb-0.5">{{ digest.date | date: '%Y-%m-%d' }} / {{ paper.arxiv_id }}</p>
    <p class="text-base font-normal lowercase tracking-tight leading-snug">{{ paper.title }}</p>
    <p class="text-xs text-black/30 mt-0.5">{{ paper.categories | join: ', ' }}</p>
  </a>
  {% endfor %}
{% endfor %}
{% if sorted.size == 0 %}
<p class="text-sm text-black/30 italic">no digests yet.</p>
{% endif %}
