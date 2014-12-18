# Create your views here.
from django.views import generic
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Case, Requirement, Project
from .serializers import CaseSerializer, RequirementSerializer, ProjectSerializer


class Index(generic.TemplateView):
    template_name = 'simple_bugs/index.html'


class CaseList(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CaseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CaseSerializer


class RequirementList(generics.ListCreateAPIView):
    queryset = Requirement.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = RequirementSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProjectSerializer



