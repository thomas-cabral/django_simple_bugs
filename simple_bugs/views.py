# Create your views here.
from django.views import generic
from .models import Bug, Requirement


class Index(generic.TemplateView):
    template_name = 'simple_bugs/index.html'


class BugList(generic.ListView):
    model = Bug
    template_name = 'simple_bugs/bug_list.html'
    context_object_name = 'bug'


class BugDetail(generic.DetailView):
    model = Bug
    template_name = 'simple_bugs/bug_detail.html'
    context_object_name = 'bug'


class RequirementList(generic.ListView):
    model = Requirement
    template_name = 'simple_bugs/requirement_list.html'
    context_object_name = 'requirement'


class RequirementDetail(generic.DetailView):
    model = Requirement
    template_name = 'simple_bugs/requirement_detail.html'
