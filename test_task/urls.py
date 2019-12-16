from django.conf.urls import url, include
from django.contrib import admin

from application import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/list/$',
        views.ApplicationListViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='test_api_list'),
    url(r'^api/item/(?P<pk>\d+)/$',
        views.ApplicationItemViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='test_api_item'),
    url(r'^api/item/(?P<pk>\d+)/update_key/$',
        views.ApplicationUpdateKeyViewSet.as_view(
            {'patch': 'partial_update', }),
        name='test_api_update_key'),
]
