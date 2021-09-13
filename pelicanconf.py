#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
from collections import OrderedDict

AUTHOR = 'harrison.ai Data Engineering Team'
SITENAME = 'harrison.ai Data Engineering Handbook'
SITEURL = ''
THEME = 'pelican-theme'

PATH = 'content'
PLUGINS = ['plugin']
LOAD_CONTENT_CACHE = False
STATIC_PATHS = ['pages', 'pages/engineering']

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_PAGES = OrderedDict()


def recursive_look(hmap, root, files):

    for idx, _root in enumerate(root):
        if _root not in hmap:
            hmap[_root] = OrderedDict()
            if idx == (len(root) - 1):
                hmap[_root]['files'] = OrderedDict()
                for fname in files:
                    hmap[_root]['files'][fname] = OrderedDict()
                return

        else:
            recursive_look(hmap[_root], root[idx + 1:], files)
            return


# Generate rank and indexes for the table of contents
for root, dirs, files in os.walk(PATH):
    files = [x for x in files if os.path.splitext(x)[1] == '.md']
    if len(files) == 0:
        continue

    root = root.replace(f'{PATH}{os.path.sep}pages', '')

    recursive_look(INDEX_PAGES, root.split(os.path.sep), files)

# TODO: Look at implementing
# Blogroll
# LINKS = (
#     ('Pelican', 'https://getpelican.com/'),
#     ('Python.org', 'https://www.python.org/'),
#     ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#     ('You can modify those links in your config file', '#'),
# )

# # Social widget
# SOCIAL = (
#     ('You can add links in your config file', '#'),
#     ('Another social link', '#'),
# )
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'marker': '[TableOfContents]',
            'title': 'Table of Contents',
            'anchorlink': True,
            'permalink': True,
            'baselevel': 2,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.tables': {}
    }
}
