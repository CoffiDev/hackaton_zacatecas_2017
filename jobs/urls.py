from django.conf.urls import url
from .views import ServicesListView

urlpatterns = [
    url(r'^young/services$', ServicesListView.as_view(), name='services_list'),
]
