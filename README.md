# django-haystack-panel

A Django Debug Toolbar panel for Haystack

## About

This is a panel for Django Debug Toolbar that displays query results from
Haystack.

## Installation

Install using `pip`:

```
pip install django-haystack-panel
```

or install the development version from source:

```
pip install git+git@github.com:streeter/django-haystack-panel.git
```

Then add `haystack_panel` to your `INSTALLED\_APPS` so that we can find the
templates in the panel. Also, add `'haystack_panel.panel.HaystackDebugPanel'`
to your `DEBUG_TOOLBAR_PANELS`.

## Usage

TODO

## Testing

There are no tests yet. Yeah, I know, I need to add some tests.
