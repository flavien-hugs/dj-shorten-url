# shortenURL/views.py

from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView,\
    DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse

from shortenURL.models import Shorten
from shortenURL.forms import ShortenForm


# CBV : Liste URL
class ListURLView(ListView):
    model = Shorten
    template_name = 'shortenURL/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Shorten.objects.order_by('-date')


# CBV : Create New URL
class CreateNewURL(CreateView):
    model = Shorten
    template_name = 'shortenURL/newurl.html'
    form_class = ShortenForm

    def get_success_url(self):
        return reverse('liste_url')


# CBV : Update URL 
class UpdateURL(UpdateView):
    model = Shorten
    form_class = ShortenForm
    template_name = 'shortenURL/updateURL.html'
    success_url = reverse_lazy('liste_url')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Shorten, code=code)

    def form_valid(self, form):
        form = ShortenForm(instance=self.get_object)
        form.save()
        return HttpResponseRedirect(self.get_success_url())


# CBV : Delete URL 
class DeleteURL(DeleteView):
    model = Shorten
    template_name = 'shortenURL/delete.html'
    success_url = reverse_lazy('liste_url')

    def form_valid(self):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Shorten, code=code)


# Fonction redirect
def redirection(request, code):
    url = get_object_or_404(Shorten, code=code)
    url.nb_acces += 1
    url.save()

    return redirect(url.url, permanent=True)
