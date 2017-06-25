from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home/index.html'), name='index'),
    url(r'^$', views.HomeView.as_view(), name='index'),
]
