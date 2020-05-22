# shortenURL/urls.py

from django.conf.urls import url
from django.urls import path
from shortenURL.views import ListURLView, CreateNewURL, UpdateURL, DeleteURL, redirection

urlpatterns = [
	path('', ListURLView.as_view(), name='liste_url'),
	path('n/', CreateNewURL.as_view(), name='new_url'),
	url(r'^edit/(?P<code>\w{6})$', UpdateURL.as_view(), name='update_url'),
	url(r'^delete/(?P<code>\w{6})$', DeleteURL.as_view(), name='delete_url'),
	url(r'^(?P<code>\w{6})/$', redirection, name='redirect_url'),
]
