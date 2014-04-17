# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Case, Requirement
from . import forms


class RequireLogin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequireLogin, self).dispatch(*args, **kwargs)


class SaveUser(RequireLogin):

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(commit=True)
        #messages.success(self.request, 'Thanks for Uploading!')
        return super(SaveUser, self).form_valid(form)


class Index(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['case_count'] = Case.objects.count()
        context['recent_bugs'] = Case.objects.filter(type='BUG', closed=False).order_by('-created_on')[:5]
        context['recent_features'] = Case.objects.filter(type='FEATURE_REQUEST', closed=False).order_by('-created_on')[:5]
        return context


class CaseList(RequireLogin, generic.ListView):
    model = Case
    template_name = 'simple_bugs/case_list.html'
    context_object_name = 'case'
    paginate_by = 10


class CaseDetail(RequireLogin, generic.DetailView):
    model = Case
    template_name = 'simple_bugs/case_detail.html'
    context_object_name = 'case'


class CaseCreate(SaveUser, generic.CreateView):
    model = Case
    form_class = forms.CaseForm
    template_name = 'simple_bugs/case_create.html'

    def get_context_data(self, **kwargs):
        context = super(CaseCreate, self).get_context_data(**kwargs)
        context['case'] = Case.objects.all().order_by('-created_on')[:5]
        return context


class CaseUpdate(RequireLogin, generic.UpdateView):
    model = Case
    form_class = forms.CaseForm
    template_name = 'simple_bugs/case_update.html'


class CaseDelete(RequireLogin, generic.DeleteView):
    model = Case


class RequirementList(RequireLogin, generic.ListView):
    model = Requirement
    template_name = 'simple_bugs/requirement_list.html'
    context_object_name = 'requirement'


class RequirementDetail(RequireLogin, generic.DetailView):
    model = Requirement
    template_name = 'simple_bugs/requirement_detail.html'


class RequirementCases(RequirementDetail):
    template_name = 'simple_bugs/requirement_cases.html'


class RequirementCreate(SaveUser, generic.CreateView):
    model = Requirement
    template_name = 'simple_bugs/requirement_create.html'
    form_class = forms.RequirementForm

    def get_context_data(self, **kwargs):
        context = super(RequirementCreate, self).get_context_data(**kwargs)
        context['requirement'] = Requirement.objects.all().order_by('-created_on')[:5]
        return context


class RequirementUpdate(RequireLogin, generic.UpdateView):
    model = Requirement
    template_name = 'simple_bugs/requirement_update.html'
    form_class = forms.RequirementForm


class RequirementDelete(RequireLogin, generic.DeleteView):
    model = Requirement


class Profile(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user_case'] = Case.objects.filter(user=self.kwargs['pk'], closed=False)
        context['user_requirement'] = Requirement.objects.filter(user=self.kwargs['pk'])
        context['assigned_case'] = Case.objects.filter(assigned_to=self.kwargs['pk'])
        return context


class SoCool(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/socool.html'

# APIs

from rest_framework import generics
from rest_framework import permissions
from .serializers import CaseSerializer, UserSerializer
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CaseAPIList(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user


class CaseAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user


class List(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/list.html'


class Detail(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/detail.html'


class New(RequireLogin, generic.TemplateView):
    template_name = 'simple_bugs/new.html'
