from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Services


class ServicesListView(ListView):

    template_name = "jobs/student_list_layout.html"
    model = Services

    def get_context_object_name(self, object_list):
        return 'services_list'

    def get_queryset(self):
        return Services.objects.all()


class ServicesDetailView(DetailView):

    template_name = "jobs/service_detail.html"
    model = Services

