# -*- coding: utf-8 -*-
# flake8: noqa (hacky way of sharing config, etc...)

from nbsite.shared_conf import *
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

extensions += [
    "nbsphinx",
    "sphinx.ext.napoleon",  # numpy-style docstrings.
    'nbsite.gallery'
]

nbsite_gallery_conf = {
    'galleries': {
        'gallery': {
            'title': 'Plotting Guide Gallery',
            'backends': [],
            'extensions': ['*.ipynb', '*.py'],
            'intro': 'Sample intro',
            'sections': [
                {'path': 'user_guide/plotting_guide',
                 'title': 'Plotting Guide',
                 'description': 'Demonstrations of plotting functions provided by GSForge.'},
            ],
        }
    },
    'github_org': 'SystemsGenetics',
    'github_project': 'GSForge',
    # 'thumbnail_url': 'https://assets.holoviews.org/thumbnails',
    # 'within_subsection_order': lambda key: key
}

project = u'GSForge'
authors = u'Tyler Biggs'
copyright = u'2019 ' + authors
description = 'Short description for html meta description.'

version = '0.0.1'
release = '0.0.1'

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
# logo file etc should be in html_static_path, e.g. assets
html_theme_options = {
    #    'custom_css':'bettercolors.css',
    #    'logo':'amazinglogo.png',
    #    'favicon':'amazingfavicon.ico'
}

_NAV = (
    ('Welcome', 'Welcome'),
    ('User Guide', 'user_guide/index'),
    # ('Gallery', 'gallery/index'),
    ('API', 'Reference_Manual/index'),
    ('Developer Guide', 'Development'),
    ('About', 'About')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'VERSION': version,
    'NAV': _NAV,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': (
        ('Github', 'https://github.com/SystemsGenetics/GSForge'),
    )
})
