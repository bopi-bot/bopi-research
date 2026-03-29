#!/usr/bin/env python3
"""Daily research digest - fetches latest AI/robotics papers from arxiv.

Handles rate limiting with exponential backoff, deduplication, date filtering.

Usage:
    python3 daily_digest.py [--date YYYY-MM-DD] [--output-dir papers/]
"""

import sys
import os
import time
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

NS = {'a': 'http://www.w3.org/2005/Atom'}

# 5 combined queries instead of 12 separate ones
QUERIES = [
    "cat:cs.RO+OR+cat:cs.AI",
    "cat:cs.LG+OR+cat:cs.CV+OR+cat:cs.CL",
    'all:"robot+learning"+OR+all:"world+model"+OR+all:"embodied+AI"',
    'all:"sim-to-real"+OR+all:"manipulation"+OR+all:"robot+navigation"',
    'all:"reinforcement+learning"+AND+all:robot',
]

MAX_RESULTS = 50
REQUEST_DELAY = 4.0  # conservative delay between requests


def fetch_url(url, retries=3):
    """Fetch URL with exponential backoff. Returns raw bytes or None."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'BopiResearch/1.0 (academic use)',
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"  rate limited, backing off {wait}s (attempt {attempt+1}/{retries})")
                time.sleep(wait)
            else:
                print(f"  HTTP {e.code}, skipping")
                return None
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"  error: {type(e).__name__}, waiting {wait}s (attempt {attempt+1}/{retries})")
            time.sleep(wait)
    return None


def search_arxiv(query):
    """Search arxiv and return parsed entries."""
    params = f"search_query={query}&max_results={MAX_RESULTS}&sortBy=submittedDate&sortOrder=descending"
    url = f"https://export.arxiv.org/api/query?{params}"
    data = fetch_url(url)
    if not data:
        return []
    try:
        root = ET.fromstring(data)
        entries = root.findall('a:entry', NS)
        return entries
    except ET.ParseError:
        print(f"  malformed XML from query, skipping")
        return []


def parse_paper(entry):
    """Parse arxiv entry to dict."""
    try:
        title = entry.find('a:title', NS).text.strip().replace('\n', ' ')
        raw_id = entry.find('a:id', NS).text.strip()
        arxiv_id = raw_id.split('/abs/')[-1].split('v')[0]
        published = entry.find('a:published', NS).text[:10]
        updated = entry.find('a:updated', NS).text[:10]
        authors = [a.find('a:name', NS).text.strip() for a in entry.findall('a:author', NS)]
        summary = entry.find('a:summary', NS).text.strip().replace('\n', ' ')
        cats = [c.get('term') for c in entry.findall('a:category', NS)]
        return {
            'arxiv_id': arxiv_id,
            'title': title,
            'authors': authors,
            'published': published,
            'updated': updated,
            'summary': summary,
            'categories': cats,
            'abs': f"https://arxiv.org/abs/{arxiv_id}",
            'pdf': f"https://arxiv.org/pdf/{arxiv_id}",
        }
    except Exception:
        return None


def fetch_all():
    """Fetch papers from all queries with delays."""
    papers = []
    for i, q in enumerate(QUERIES):
        label = q[:50] + ('...' if len(q) > 50 else '')
        print(f"  [{i+1}/{len(QUERIES)}] {label}")
        entries = search_arxiv(q)
        for entry in entries:
            p = parse_paper(entry)
            if p:
                papers.append(p)
        if i < len(QUERIES) - 1:
            time.sleep(REQUEST_DELAY)
    return papers


def main():
    target_date = datetime.utcnow().strftime('%Y-%m-%d')
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == '--date' and i < len(sys.argv):
            target_date = sys.argv[i + 1]
            break

    output_dir = 'papers'
    os.makedirs(output_dir, exist_ok=True)

    print(f"=== daily digest: {target_date} ===\n")

    papers = fetch_all()
    print(f"\nraw fetch: {len(papers)}")

    # dedup
    seen = set()
    unique = [p for p in papers if not (p['arxiv_id'] in seen or seen.add(p['arxiv_id']))]
    print(f"deduped: {len(unique)}")

    # date filter (allow 1 day before for timezone edge cases)
    cutoff = (datetime.strptime(target_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    filtered = [p for p in unique if p['published'] >= cutoff]
    filtered.sort(key=lambda p: p['published'], reverse=True)
    print(f"after date filter: {len(filtered)}")

    # write digest
    path = os.path.join(output_dir, f"{target_date}.md")
    with open(path, 'w') as f:
        f.write(f"# daily digest - {target_date}\n\n")
        f.write(f"{len(filtered)} papers.\n\n---\n\n")
        for i, p in enumerate(filtered, 1):
            f.write(f"## {i}. {p['title']}\n\n")
            f.write(f"**arxiv:** [{p['arxiv_id']}]({p['abs']}) | **published:** {p['published']}\n\n")
            auth = ', '.join(p['authors'][:5])
            if len(p['authors']) > 5:
                auth += f" et al. ({len(p['authors'])} total)"
            f.write(f"**authors:** {auth}\n\n")
            f.write(f"**categories:** {', '.join(p['categories'])}\n\n")
            f.write(f"### problem space\n\n{p['summary']}\n\n")
            f.write(f"### methods\n\n*tbd*\n\n")
            f.write(f"### evaluation\n\n*tbd*\n\n")
            f.write(f"### links\n\n- paper: {p['abs']}\n- pdf: {p['pdf']}\n- code: *tbd*\n- website: *tbd*\n\n")
            f.write(f"### reproduction guide\n\n*tbd*\n\n---\n\n")

    summary = {'date': target_date, 'count': len(filtered),
               'papers': [{'id': p['arxiv_id'], 'title': p['title']} for p in filtered]}
    with open(os.path.join(output_dir, f"{target_date}.json"), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n-> {path} ({len(filtered)} papers)")


if __name__ == '__main__':
    main()
