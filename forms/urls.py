from django.urls import path

from . import views
from . import forms


urlpatterns = [
    path('', views.forms_index),
    path('search/', views.search_form),
    path('file/', views.file_input),
    path('model/', views.model_input),
    path('add-author/', views.add_author),
    path('add-article/', views.add_article),
    path('generic-form/', views.ContactFormView.as_view()),
    path('validators-form/', views.UrlView.as_view()),
    path('function-form/', views.function_form, name='function_form'),
    path('class-form/', views.ClassFormView.as_view(), name='class_form'),
    path('model-form/', views.ModelFormView.as_view(), name='model_form')
]

# urlpatterns = [
#      # url(r'^$', views.form),
#      url(r'^$', views.ContactFormView.as_view()),
#      url(r'^url-form$', views.UrlView.as_view()),
#      url(r'^test-view$', views.test_view),
#      url(r'^search-form/$', views.search_form ),
#      url(r'^file-input/$', views.file_input ),
#      url(r'^search/$', views.search),
#      url(r'^add-article/$', views.add_article),
#      url(r'^add-author/$', views.author_add),




