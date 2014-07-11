from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from simple_bugs.groups.models import Group
from simple_bugs.projects.models import Project

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

    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        group = Group.objects.filter(user__id=self.request.user.id)
        form = super(RequirementCreate, self).get_form(form_class)
        form.fields['working_on'].queryset = User.objects.filter(group_user_list=group)
        form.fields['project'].queryset = Project.objects.filter(group__user__id=self.request.user.id)
        return form



class RequirementUpdate(TrackUser, generic.UpdateView):
    #model = Requirement
    template_name = 'requirements/requirement_update.html'
    form_class = forms.RequirementForm

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)

    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        group = Requirement.objects.filter(project__group__user__id=self.request.user.id)
        form = super(RequirementUpdate, self).get_form(form_class)
        form.fields['working_on'].queryset = User.objects.filter(group_user_list=group)
        form.fields['project'].queryset = Project.objects.filter(group__user__id=self.request.user.id)
        return form


class RequirementDelete(RequireLogin, generic.DeleteView):
    model = Requirement
