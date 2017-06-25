from django.shortcuts import redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Services
from django.contrib import messages


class ServicesListView(ListView):

    template_name = "jobs/student_list_layout.html"
    model = Services

    def get_context_object_name(self, object_list):
        return 'services_list'

    def get_queryset(self):

        print self.request.user
        return Services.objects.all()


class ServicesDetailView(DetailView):

    template_name = "jobs/service_detail.html"
    model = Services

    def get_context_data(self, **kwargs):
        context = super(ServicesDetailView, self).get_context_data(**kwargs)

        user = self.request.user

        context['young_id'] = user.youngprofile.pk
        context['userIsAcepted'] = user.youngprofile in context['object'].youngs_registered.all()
        context['userHasRequested'] = user.youngprofile in context['object'].youngs_requests.all()
        context['canApply'] = (user.youngprofile.level == context['object'].level
                               and user.youngprofile.interest_area == context['object'].interest_area)

        return context


class ApplyView(View):

    def post(self, request):
        profile = self.request.user.youngprofile.pk
        try:
            service = Services.objects.get(pk=request.POST['service'])
        except Exception as e:
            return redirect('services_list')

        service.youngs_requests.add(profile)
        messages.add_message(request, messages.INFO, 'Tu solicitud fue enviada')
        return redirect('service_detail', pk=service.pk)