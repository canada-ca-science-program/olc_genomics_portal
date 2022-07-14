from django.urls import re_path as url


from . import views

urlpatterns = [
    url(r'^$',views.UserListView.as_view(),name='list'),
    url(r'^~redirect/$',views.UserRedirectView.as_view(),name='redirect'),
    url(r'^(?P<username>[\w.@+-]+)/$',views.UserDetailView.as_view(),name='detail'),
    url(r'^~update/$',views.UserUpdateView.as_view(),name='update'),
]
