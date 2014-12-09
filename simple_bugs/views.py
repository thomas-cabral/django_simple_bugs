# Create your views here.
from django.views import generic
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Case, Requirement, Project, Comment
from .serializers import CaseSerializer, RequirementSerializer, ProjectSerializer, CommentSerializer


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


class Index(generic.TemplateView):
    template_name = 'simple_bugs/index.html'


class CaseList(generics.ListCreateAPIView):
    model = Case
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CaseSerializer


class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Case
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CaseSerializer


class RequirementList(generics.ListCreateAPIView):
    model = Requirement
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = RequirementSerializer


class ProjectList(generics.ListCreateAPIView):
    model = Project
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProjectSerializer


class CommentList(generics.ListCreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
