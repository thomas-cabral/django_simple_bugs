# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from simple_bugs.cases.models import Case, TestCase
from simple_bugs.projects.models import Project
from simple_bugs.requirements.models import Requirement
from simple_bugs.projects.serializers import ProjectSerializer
from simple_bugs.groups.models import Group
from simple_bugs.estimates.models import Estimate


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
        context['recent_bugs'] = Case.objects.filter(project__group__user__id=self.request.user.id, type='BUG',
                                                     closed=False).order_by('-created_on')[:10]
        context['recent_features'] = Case.objects.filter(
            project__group__user__id=self.request.user.id,
            type='FEATURE_REQUEST', closed=False).order_by('-created_on')[:10]
        return context


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

# APIs

from rest_framework import permissions, generics, filters
from .serializers import UserSerializer
from simple_bugs.requirements.serializers import RequirementSerializer
from simple_bugs.cases.serializers import CaseSerializer, TestCaseSerializer
from django.contrib.auth.models import User


class RequirementsApiList(generics.ListAPIView):
    serializer_class = RequirementSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Requirement.objects.filter(project__group__user__id=user.id)


class RequirementsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequirementSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Requirement.objects.filter(project__group__user__id=user.id)


class CaseAPIList(generics.ListCreateAPIView):
    serializer_class = CaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'detail', 'user__username', 'pk',)

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_queryset(self):
        return Case.objects.filter().order_by('closed')


class CaseAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_queryset(self):
        user = self.request.user
        return Case.objects.filter(project__group__user__id=user.id)


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Project


class ProjectDetail(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Project


class TestCaseDetail(generics.RetrieveAPIView):
    serializer_class = TestCaseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = TestCase


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)