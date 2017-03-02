from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from words.forms import WordsForm


class HomePage(FormView):
    template_name = 'index.html'
    form_class = WordsForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):

        print('hello')
        self.request.session['results'] = 'hello!'
        return super().form_valid(form)

