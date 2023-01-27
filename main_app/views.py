from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Pierogi

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class AllPierogi(TemplateView):
    template_name = 'all_pierogi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pierogi'] = pierogi
        context["pierogi"] = Pierogi.objects.all()
        filling = self.request.GET.get("filling")
        if filling != None and filling != "":
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["pierogi"] = Pierogi.objects.filter(
                filling__icontains=filling)
            context["header"] = f'Results for "{filling}"'
        else:
            context["pierogi"] = Pierogi.objects.all()
            context["header"] = "All Pierogi"
        return context


class PierogiDetail(DetailView):
    model = Pierogi
    template_name = 'pierogi_detail.html'


class PierogiCreate(CreateView):
    model = Pierogi
    fields = ['filling', 'method', 'image']
    template_name = 'pierogi_create.html'

    def get_success_url(self):
        return reverse('pierogi_detail', kwargs={'pk': self.object.pk})


class PierogiUpdate(UpdateView):
    model = Pierogi
    fields = ['filling', 'method', 'image']
    template_name = 'pierogi_edit.html'

    def get_success_url(self):
        return reverse('pierogi_detail', kwargs={'pk': self.object.pk})


class PierogiDelete(DeleteView):
    model = Pierogi
    template_name = 'pierogi_delete_confirmation.html'
    success_url = "/pierogi/"
