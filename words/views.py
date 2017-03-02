from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from words.forms import WordsForm
from words.words import Word


class HomePage(FormView):
    template_name = 'index.html'
    form_class = WordsForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):

        input_text = form.cleaned_data['text']
        result = Word().get_concordanse(input_text)
        self.request.session['results'] = result
        return super().form_valid(form)

