# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from simple_bugs.cases.models import Case
from simple_bugs.requirements.models import Requirement
from simple_bugs.estimates.models import Estimate
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


class Index(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['case_count'] = Case.objects.filter(project__group__user__id=self.request.user.id).count()
        context['recent_bugs'] = Case.objects.filter(project__group__user__id=self.request.user.id, type='BUG', closed=False).order_by('-created_on')[:10]
        context['recent_features'] = Case.objects.filter(project__group__user__id=self.request.user.id, type='FEATURE_REQUEST', closed=False).order_by('-created_on')[:10]
        return context


class CaseList(RequireLogin, generic.ListView):
    template_name = 'simple_bugs/case_list.html'
    paginate_by = 10
    context_object_name = 'case'

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id, closed=False)


class CaseDetail(RequireLogin, generic.DetailView):
    #model = Case
    template_name = 'simple_bugs/case_detail.html'
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
    template_name = 'simple_bugs/case_create.html'

    def get_context_data(self, **kwargs):
        context = super(CaseCreate, self).get_context_data(**kwargs)
        context['case'] = Case.objects.filter(project__group__user__id=self.request.user.id).order_by('-created_on')[:5]
        return context


class CaseUpdate(TrackUser, generic.UpdateView):
    #model = Case
    form_class = forms.CaseForm
    template_name = 'simple_bugs/case_update.html'

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id)


class CaseDelete(RequireLogin, generic.DeleteView):
    #model = Case

    def get_queryset(self):
        return Case.objects.filter(project__group__user__id=self.request.user.id)


class RequirementList(RequireLogin, generic.ListView):
    #model = Requirement
    template_name = 'simple_bugs/requirement_list.html'
    context_object_name = 'requirement'

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementDetail(RequireLogin, generic.DetailView):
    #model = Requirement
    template_name = 'simple_bugs/requirement_detail.html'

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementCases(RequirementDetail):
    template_name = 'simple_bugs/requirement_cases.html'

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementCreate(SaveUser, generic.CreateView):
    model = Requirement
    template_name = 'simple_bugs/requirement_create.html'
    form_class = forms.RequirementForm

    def get_context_data(self, **kwargs):
        context = super(RequirementCreate, self).get_context_data(**kwargs)
        context['requirement'] = Requirement.objects.filter(project__group__user__id=self.request.user.id).order_by('-created_on')[:5]
        return context


class RequirementUpdate(TrackUser, generic.UpdateView):
    #model = Requirement
    template_name = 'simple_bugs/requirement_update.html'
    form_class = forms.RequirementForm

    def get_queryset(self):
        return Requirement.objects.filter(project__group__user__id=self.request.user.id)


class RequirementDelete(RequireLogin, generic.DeleteView):
    model = Requirement


class Profile(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user_case'] = Case.objects.filter(project__group__user__id=self.request.user.id, user__username=self.kwargs['username'])
        context['user_requirement'] = Requirement.objects.filter(project__group__user__id=self.request.user.id,
                                                                 working_on__username=self.kwargs['username'])
        context['assigned_case'] = Case.objects.filter(project__group__user__id=self.request.user.id,
                                                       assigned_to__username=self.kwargs['username'])
        return context


class SoCool(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/socool.html'

# APIs

from rest_framework import permissions, generics, filters
from .serializers import CaseSerializer, UserSerializer, RequirementSerializer
from django.contrib.auth.models import User


class RequirementsApiList(generics.ListAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RequirementsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CaseAPIList(generics.ListCreateAPIView):
    queryset = Case.objects.filter(closed=False)
    serializer_class = CaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'detail', 'user__username', 'pk',)

    def pre_save(self, obj):
        obj.user = self.request.user


class CaseAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class List(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/list.html'


class Detail(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/detail.html'


class New(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/new.html'


class Search(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/search.html'