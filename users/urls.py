from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login$', TemplateView.as_view(template_name='users/login.html'), name='login'),
    url(r'^signup$', TemplateView.as_view(template_name='users/signup.html'), name='signup'),
]
