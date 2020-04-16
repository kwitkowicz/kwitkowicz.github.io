#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Krzysiek Witkowicz'
SITENAME = u'Krzysiek Witkowicz'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'Polish'

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
SOCIAL = (('github', 'http://github.com/kwitkowicz'),)

THEME = "../pelican-themes/pelican-bootstrap3"
# JINJA_EXTENSIONS = ['jinja2.ext.i18n']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud', 'render_math',
           'better_figures_and_images', 'series']
# SERIES_TEXT = ' %(index)s of the %(name)s series'
# SERIES_TEXT = "Część %(index)s serii: %(name)s"
# DISPLAY_SERIES_ON_SIDEBAR = 'True'
# SHOW_SERIES = 'True'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
STATIC_PATHS = ['images', 'pdfs']
PYGMENTS_STYLE = 'solarizeddark'
BOOTSTRAP_NAVBAR_INVERSE = 'True'
CC_LICENSE = 'CC-BY-SA'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5
BOOTSTRAP_THEME = 'cosmo'
SHOW_ARTICLE_CATEGORY = 'True'
DISPLAY_ARTICLE_INFO_ON_INDEX = 'True'
