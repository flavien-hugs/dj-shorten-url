# shortenURL/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from shortenURL.models import Shorten
from shortenURL.forms import ShortenForm


# CBV : Liste URL
class ListURLView(ListView):
    model = Shorten
    template_name = 'shortenURL/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Shorten.objects.order_by('-nb_acces')


# CBV : Create New URL
class CreateNewURL(CreateView):
    model = Shorten
    template_name = 'shortenURL/newurl.html'
    form_class = ShortenForm
    success_url = reverse_lazy('liste_url')


# CBV : Update URL 
class UpdateURL(UpdateView):
    model = Shorten
    template_name = 'shortenURL/newurl.html'
    form_class = ShortenForm
    success_url = reverse_lazy('liste_url')

    def form_valid(self, form):
        form.save()
        message.success(self.request, "Mise à jour effectuée avec succès.")
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Shorten, code=code)


# CBV : Delete URL 
class DeleteURL(DeleteView):
    model = Shorten
    template_name = 'shortenURL/delete.html'
    success_url = reverse_lazy('liste_url')

    def form_valid(self, queryset=None):
        self.object = form.save()
        message.success(self.request, "Mise à jour effectuée avec succès.")
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Shorten, code=code)


# CBV : Redirect URL
class RedirectURL(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        url = get_object_or_404(Shorten, code=code)
        url.nb_acces += 1
        url.save()
        return super().get_redirect_url(*args, **kwargs)
