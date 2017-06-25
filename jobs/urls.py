from django.conf.urls import url
from .views import ServicesListView, ServicesDetailView, ApplyView

urlpatterns = [
    url(r'^young/services$', ServicesListView.as_view(), name='services_list'),
    url(r'^young/services/(?P<pk>\w+)$', ServicesDetailView.as_view(), name='service_detail'),
    url(r'^apply', ApplyView.as_view(), name="apply")
]
