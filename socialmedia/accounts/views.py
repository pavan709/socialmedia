from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,
                                  ListView,UpdateView,
                                  DetailView,DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from . import forms
from django.http import Http404
from posts import models
# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class UserList(ListView,LoginRequiredMixin):
    model = models.Post
    select_related = ('user', 'group')
    template_name = 'accounts/about_user.html'
    # queryset = models.Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:

            context['user_groups'] = models.Group.objects.filter(members__in=[self.kwargs.get('pk')])
            context['posts'] = models.Post.objects.filter(user__in=[self.kwargs.get('pk')])
            context['username'] = User.objects.get(pk=self.kwargs.get('pk')).username
        except :
            raise Http404

        return context
