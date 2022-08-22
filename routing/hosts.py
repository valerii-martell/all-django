from django_hosts import patterns, host

from all_django import settings
from . import subd_urls_api, subd_urls_beta
from .views import api, beta

host_patterns = patterns(
    "",
    host(r"www", settings.ROOT_URLCONF, name="www"),
    host(r"api", subd_urls_api, name="host_api"),
    host(r"beta", subd_urls_beta, name="host_beta"),
)
