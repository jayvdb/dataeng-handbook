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

        v = hmap[k]

        for page in v:

            # Skip drafts
            if 'url' not in page:
                continue

            if page['filename'] == 'index.md':
                msg = f"<a href=\"./{page['url']}\" "
                msg += "data-toggle=\"collapse\" aria-expanded=\"false\" class=\"dropdown-toggle\""
                msg += f">{page['category']}</a>"
                msg += f"<ul class=\"list-unstyled\" id=\"{page['title'].replace(' ', '')}\">"
                toc.append(msg)

            else:
                msg = f"<li><a href=\"./{page['url']}\">{page['title']}</a></li>"
                toc.append(msg)

        toc.append('</ul>')
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
