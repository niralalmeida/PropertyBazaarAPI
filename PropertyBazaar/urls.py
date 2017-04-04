from django.conf.urls import url
from PropertyBazaar.views import PropertyList, PropertyDetail, UserDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^property/$', PropertyList.as_view(), name='property-list'),
    url(r'^property/(?P<pk>[0-9]+)/$', PropertyDetail.as_view(), name='property-detail'),
    url(r'^user/$', UserList.as_view(), name='user-list'),
    url(r'^user/(?P<username>[a-zA-Z]+)/$', UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)