#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import os

from pelican import signals


def apply_url(hmap, keys, url, title, category, categories):

    for k in keys:
        if k in hmap:
            apply_url(hmap[k], keys[1:], url, title, category, categories)
            return
        elif k in hmap.get('files', []):
            hmap['files'][k]['url'] = url if url is not None else ''
            hmap['files'][k]['title'] = title
            hmap['files'][k]['category'] = category

            if category.name not in categories:
                categories[category.name] = []

            payload = {
                'url': url if url is not None else '',
                'title': title,
                'category': category,
                'filename': k
            }
            if k == 'index.md':
                categories[category.name].insert(0, payload)
            else:
                categories[category.name].append(payload)

            return


def get_toc(hmap, toc, site_url):

    keys = list(hmap.keys())

    if 'Home' in keys:
        keys.remove('Home')

    # Do files first
    for k in ['Home'] + keys:

        if k not in hmap:
            continue

        # Skip drafts
        pages = list(p for p in hmap[k] if "url" in p)

        if len(pages) == 0:
            continue

        if pages[0]['filename'] != 'index.md':
            print("WARNING: the first file in a category must be `index.md`, otherwise we will generate garbage HTML.")
            print(f"Category {repr(k)} has files {list(p['filename'] for p in pages)}")
            print("Cowardly refusing to include it in the ToC.")
            continue

        for page in pages:

            if page['filename'] == 'index.md':
                msg = f"<a href=\"{site_url}/{page['url']}\" "
                msg += "data-toggle=\"collapse\" aria-expanded=\"false\" class=\"dropdown-toggle\""
                msg += f">{page['category']}</a>"
                msg += f"<ul class=\"list-unstyled\" id=\"{page['title'].replace(' ', '')}\">"
                toc.append(msg)

            else:
                msg = f"<li><a href=\"{site_url}/{page['url']}\">{page['title']}</a></li>"
                toc.append(msg)

        toc.append('</ul>')


def gen_toc(page_generator):

    categories = {}

    for page in page_generator.pages:
        _path = page.relative_source_path.replace('pages', '')
        if not hasattr(page, 'tocignore'):
            apply_url(page_generator.settings['INDEX_PAGES'],
                      _path.split(os.path.sep), page.url, page.title,
                      page.category, categories)

    page_generator.context['TOC'] = []
    get_toc(categories, page_generator.context['TOC'],
            page_generator.settings['SITEURL'])


def register():
    signals.page_generator_finalized.connect(gen_toc)
