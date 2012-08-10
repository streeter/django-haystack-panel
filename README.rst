Django Haystack Panel
=====================

A Django Debug Toolbar panel for Haystack

About
-----

This is a panel for `Django Debug Toolbar`_ that displays query results from
Haystack.

Installation
------------

Install using ``pip``::

    pip install django-haystack-panel

or install the development version from source::

    pip install git+git@github.com:streeter/django-haystack-panel.git

Then add ``haystack_panel`` to your ``INSTALLED\_APPS`` so that we can find the
templates in the panel. Also, add ``'haystack_panel.panel.HaystackDebugPanel'``
to your ``DEBUG_TOOLBAR_PANELS``.

Usage
-----

TODO

Testing
-------

There are no tests yet. Yeah, I know, I need to add some tests. However,
this has been tested with Haystack version 2.0. I also expect it to work on
at least Haystack >= 1.2.x. Let me know if other versions also work.


.. _Django Debug Toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
