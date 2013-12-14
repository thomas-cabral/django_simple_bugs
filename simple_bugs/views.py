# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Bug, Requirement
import forms


class RequireLogin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequireLogin, self).dispatch(*args, **kwargs)


class SaveUser(object):

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(commit=True)
        #messages.success(self.request, 'Thanks for Uploading!')
        return super(SaveUser, self).form_valid(form)


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


class BugCreate(SaveUser, generic.CreateView):
    model = Bug
    form_class = forms.BugForm
    template_name = 'simple_bugs/bug_create.html'


class BugUpdate(generic.CreateView):
    model = Bug


class BugDelete(generic.DeleteView):
    model = Bug


class RequirementList(generic.ListView):
    model = Requirement
    template_name = 'simple_bugs/requirement_list.html'
    context_object_name = 'requirement'


class RequirementDetail(generic.DetailView):
    model = Requirement
    template_name = 'simple_bugs/requirement_detail.html'


class RequirementCreate(generic.CreateView):
    model = Requirement


class RequirementUpdate(generic.UpdateView):
    model = Requirement


class RequirementDelete(generic.DeleteView):
    model = Requirement
