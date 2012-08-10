from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from debug_toolbar.panels import DebugPanel

try:
    from haystack.backends import queries
    haystack_version = 1
except ImportError:
    from haystack import connections
    haystack_version = 2


class HaystackDebugPanel(DebugPanel):
    """
    Panel that displays queries made by Haystack backends.
    """
    name = 'Haystack'
    template = 'haystack_panel/haystack_panel.html'
    has_content = True

    def _get_query_count(self):
        if haystack_version == 1:
            return len(queries)
        else:
            return sum(map(lambda conn: len(conn.queries), connections.all()))

    def nav_title(self):
        return _('Haystack Queries')

    def nav_subtitle(self):
        return "%s queries" % self._get_query_count()

    def url(self):
        return ''

    def title(self):
        return self.nav_title()

    def get_context(self):
        query_list = []

        if haystack_version == 1:
            query_list = [q for q in queries]
        else:
            query_list = [q for conn in connections.all() for q in conn.queries]
            query_list.sort(key=lambda q: q['start'])

        return {
            'queries': query_list,
            'debug': getattr(settings, 'DEBUG', False),
        }

    def process_response(self, request, response):
        if hasattr(self, 'record_stats'):
            self.record_stats(self.get_context())

    def content(self):
        if hasattr(self, 'record_stats'):
            return super(HaystackDebugPanel, self).content()
        else:
            context = self.context.copy()
            context.update(self.get_context())
            return render_to_string(self.template, context)
