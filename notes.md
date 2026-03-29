---
layout: default
title: notes
permalink: /notes/
---

<h1 class="text-2xl font-normal lowercase tracking-tight mb-8">notes</h1>

{% assign sorted = site.notes | sort: 'date' | reverse %}
{% for note in sorted %}
<a href="{{ note.url | relative_url }}" class="block py-4 border-b border-black/10 first:pt-0 hover:text-bolt transition-colors">
  <p class="text-xs text-black/40 mb-0.5">{{ note.date | date: '%Y-%m-%d' }} / {{ note.source }} / {{ note.type }}</p>
  <p class="text-base font-normal lowercase tracking-tight leading-snug">{{ note.title }}</p>
</a>
{% endfor %}
{% if sorted.size == 0 %}
<p class="text-sm text-black/30 italic">no notes yet.</p>
{% endif %}
