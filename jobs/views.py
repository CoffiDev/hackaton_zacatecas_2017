from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ServicesListView(ListView):

    template_name = "jobs/student_list_layout.html"

    def get_context_object_name(self, object_list):
        return 'services_list'

    def get_queryset(self):
        return [{
            "title": "Mejorar proceso de distribucion"
        }, {
            "title": "Administrar mas optimamente los recursos"
        }]


class ServicesDetailView(DetailView):

    template_name = "jobs/service_detail.html"

    def get_object(self, queryset=None):
        return {"title": "Mejorar procesos"}
