from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from .models import Case
from . import forms
from simple_bugs.estimates.models import Estimate
from simple_bugs.groups.models import Group
from simple_bugs.projects.models import Project
from simple_bugs.requirements.models import Requirement


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


class CaseList(RequireLogin, generic.ListView):
    template_name = 'cases/case_list.html'
    paginate_by = 10
    context_object_name = 'case'

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id, closed=False)


class CaseDetail(RequireLogin, generic.DetailView):
    #model = Case
    template_name = 'cases/case_detail.html'
    context_object_name = 'case'

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(CaseDetail, self).get_context_data(**kwargs)
        context['estimate_list'] = Estimate.objects.filter(case__id=self.kwargs['pk'])
        return context


class CaseCreate(SaveUser, generic.CreateView):
    model = Case
    form_class = forms.CaseForm
    template_name = 'cases/case_create.html'

    def get_context_data(self, **kwargs):
        context = super(CaseCreate, self).get_context_data(**kwargs)
        context['case'] = Case.objects.filter(project__group__user__id=self.request.user.id).order_by('-created_on')[:5]
        return context

    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        group = Group.objects.filter(user__id=self.request.user.id)
        form = super(CaseCreate, self).get_form(form_class)
        form.fields['assigned_to'].queryset = User.objects.filter(group_user_list=group)
        form.fields['project'].queryset = Project.objects.filter(group__user__id=self.request.user.id)
        form.fields['requirement'].queryset = Requirement.objects.filter(project__group__user__id=group)
        return form


class CaseUpdate(TrackUser, generic.UpdateView):
    #model = Case
    form_class = forms.CaseForm
    template_name = 'cases/case_update.html'

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id)

    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        group = Group.objects.filter(user__id=self.request.user.id)
        form = super(CaseUpdate, self).get_form(form_class)
        form.fields['assigned_to'].queryset = User.objects.filter(group_user_list=group)
        form.fields['project'].queryset = Project.objects.filter(group__user__id=self.request.user.id)
        form.fields['requirement'].queryset = Requirement.objects.filter(project__group__user__id=group)
        return form


class CaseDelete(RequireLogin, generic.DeleteView):
    #model = Case

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id)