---
layout: default
title: angles
permalink: /angles/
---

<h1 class="text-2xl font-normal lowercase tracking-tight mb-8">angles</h1>

{% assign active = site.angles | where: 'status', 'active' | sort: 'date' | reverse %}
{% assign archived = site.angles | where: 'status', 'archived' | sort: 'date' | reverse %}

{% if active.size > 0 %}
<h2 class="text-sm font-medium uppercase tracking-wider text-black/40 mb-4">active</h2>
{% for angle in active %}
<a href="{{ angle.url | relative_url }}" class="block py-3 border-b border-black/10 hover:text-bolt transition-colors">
  <p class="text-base font-normal lowercase tracking-tight leading-snug">{{ angle.title }}</p>
  <p class="text-xs text-black/30 mt-0.5">{{ angle.date | date: '%Y-%m-%d' }} / {{ angle.source }}</p>
</a>
{% endfor %}
{% endif %}

{% if archived.size > 0 %}
<h2 class="text-sm font-medium uppercase tracking-wider text-black/40 mb-4 mt-8">archived</h2>
{% for angle in archived %}
<a href="{{ angle.url | relative_url }}" class="block py-3 border-b border-black/10 hover:text-bolt transition-colors">
  <p class="text-base font-normal lowercase tracking-tight leading-snug">{{ angle.title }}</p>
  <p class="text-xs text-black/30 mt-0.5">{{ angle.date | date: '%Y-%m-%d' }} / {{ angle.source }}</p>
</a>
{% endfor %}
{% endif %}

{% if active.size == 0 and archived.size == 0 %}
<p class="text-sm text-black/30 italic">no angles yet.</p>
{% endif %}
