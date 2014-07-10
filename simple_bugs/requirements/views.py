from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Requirement
from . import forms


class RequireLogin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequireLogin, self).dispatch(*args, **kwargs)


class SaveUser(RequireLogin):
    """
    Mixin to save user to model
    """

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(commit=True)
        return super(SaveUser, self).form_valid(form)


class TrackUser(RequireLogin):
    """
    Mixin for tracking user on change
    """

    def form_valid(self, form):
        form.instance.changed_by = self.request.user
        form.save(commit=True)
        return super(TrackUser, self).form_valid(form)


class RequirementList(RequireLogin, generic.ListView):
    #model = Requirement
    template_name = 'requirements/requirement_list.html'
    context_object_name = 'requirement'

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementDetail(RequireLogin, generic.DetailView):
    #model = Requirement
    template_name = 'requirements/requirement_detail.html'

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementCases(RequirementDetail):
    template_name = 'requirements/requirement_cases.html'

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementCreate(SaveUser, generic.CreateView):
    model = Requirement
    template_name = 'requirements/requirement_create.html'
    form_class = forms.RequirementForm

    def get_context_data(self, **kwargs):
        context = super(RequirementCreate, self).get_context_data(**kwargs)
        context['requirement'] = Requirement.objects.filter(project__group__user__id=self.request.user.id).order_by('-created_on')[:5]
        return context


class RequirementUpdate(TrackUser, generic.UpdateView):
    #model = Requirement
    template_name = 'requirements/requirement_update.html'
    form_class = forms.RequirementForm

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementDelete(RequireLogin, generic.DeleteView):
    model = Requirement
