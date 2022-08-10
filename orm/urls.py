from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('list/', views.List.as_view(), name='list'),
    path('upload/', views.upload_data, name='upload'),
    path('filter/', views.FilterView.as_view(), name='filter'),
    path('relation-filter/', views.relation_filter_view, name='relation_filter'),
    path('exclude/', views.ExcludeView.as_view(), name='exclude'),
    path('orderby/', views.OrderByView.as_view(), name='orderby'),
    path('all/', views.AllView.as_view(), name='all'),
    path('union/', views.UnionView.as_view(), name='union'),
    path('none/', views.NoneView.as_view(), name='none'),
    path('values/', views.ValuesView.as_view(), name='values'),
    path('dates/', views.date_view, name='dates'),
    path('get/', views.get_view, name='get'),
    path('create/', views.create_view, name='create'),
]

# urlpatterns = [
#
#     url(r'^$' , List.as_view() , name = 'list-view'),
#
# ]
