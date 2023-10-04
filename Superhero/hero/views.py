from typing import Any
from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        kwargs['doc'] = 'abc'
        return super().get_context_data(**kwargs)