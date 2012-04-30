from django.views.generic.edit import CreateView

from . import models


class Index(CreateView):
    template_name = 'index.html'
    model = models.Some
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['some_list'] = models.Some.objects.all()
        return context

index = Index.as_view()

