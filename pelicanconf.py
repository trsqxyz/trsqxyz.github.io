#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TRS'
SITENAME = 'trsqxyz.github.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'jp'
DATE_FORMATS = {
    'en': '%Y-%m-%d %H:%M',
    'jp': '%Y-%m-%d %H:%M',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/trss/'),
          ('Instagram', 'https://instagr.am/trss/'),
          ('Tumblr', 'https://trss.tumblr.com/'),
          ('Photograph', 'https://nyis.tumblr.com/'),
          ('Blog', 'https://trss.hatenablog.com'),
          )

DEFAULT_PAGINATION = 10

THEME = 'mytheme/notmyidea'
TWITTER_USERNAME = 'trss'
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
