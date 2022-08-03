from django.conf.urls.static import static
from .views import List
from django.urls import path

urlpatterns = [
    path('', List.as_view()),
]

# urlpatterns = [
#
#     url(r'^$' , List.as_view() , name = 'list-view'),
#
# ]
