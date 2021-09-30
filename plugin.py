#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import os

from pelican import signals


def apply_url(hmap, keys, url, title, category):

    for k in keys:
        if k in hmap:
            apply_url(hmap[k], keys[1:], url, title, category)
            return
        elif k in hmap['files']:
            hmap['files'][k]['url'] = url if url is not None else ''
            hmap['files'][k]['title'] = title
            hmap['files'][k]['category'] = category
            return


def get_toc(hmap, toc, site_url, level=0):

    keys = list(hmap.keys())
    keys.pop(keys.index('files'))

    # Do files first
    for k in ['files'] + keys:
        v = hmap[k]

        if k == 'files':

            files = list(v.keys())

            if 'index.md' in files:
                _v = v['index.md']

                # Skip drafts
                if 'url' not in _v:
                    continue
                files.pop(files.index('index.md'))
                msg = f"<a href=\"{site_url}/{_v['url']}\" "
                msg += f"data-toggle=\"collapse\" aria-expanded=\"false\" class=\"dropdown-toggle\""
                msg += f">{_v['category']}</a>"
                msg += f"<ul class=\"list-unstyled\" id=\"{_v['title'].replace(' ', '')}\">"
                toc.append(msg)

            for _k in files:
                _v = v[_k]

                # Skip drafts
                if 'url' not in _v:
                    continue
                msg = f"<li><a href=\"{site_url}/{_v['url']}\">{_v['title']}</a></li>"
                toc.append(msg)
            toc.append('</ul>')

        else:
            get_toc(v, toc, site_url, level + 1)


def func2(page_generator):

    categories = set()

    for page in page_generator.pages:
        _path = page.relative_source_path.replace('pages', '')
        apply_url(page_generator.settings['INDEX_PAGES'],
                  _path.split(os.path.sep), page.url, page.title,
                  page.category)
        categories.add(page.category)

    page_generator.context['TOC'] = []
    get_toc(page_generator.settings['INDEX_PAGES'][''],
            page_generator.context['TOC'], page_generator.settings['SITEURL'])


def register():
    signals.page_generator_finalized.connect(func2)
