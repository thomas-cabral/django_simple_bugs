from django.views import generic
from simple_bugs.views import RequireLogin


class Index(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/angular/angular_index.html'


class List(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/angular/list.html'


class Detail(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/angular/detail.html'


class New(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/angular/new.html'