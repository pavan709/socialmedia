from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin, PrefetchRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

# Group post list
# class PostList(SelectRelatedMixin, generic.ListView):
#     model = models.Post
#     select_related = ('user', 'group')
#     template_name = 'posts/post_list.html'
#     # queryset = models.Post.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             context['user_groups'] = models.Group.objects.filter(members__in=[self.request.user])
#             context['other_groups'] = models.Group.objects.exclude(members__in=[self.request.user])
#         except:
#             context['other_groups'] = models.Group.objects.all()
#         return context


# user post list
# class UserPosts(generic.ListView):
#     model = models.Post
#     template_name = 'posts/user_post_list.html'
#
#     def get_queryset(self):
#         try:
#             self.post_user = User.objects.prefetch_related("posts").get(username__iexact=self.kwargs.get('username',''))
#             # self.post_user = User.objects.prefetch_related("posts").get(username__iexact=self.kwargs['username'])
#
#         except User.DoesNotExist:
#             raise Http404
#         else:
#             return self.post_user.posts.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_user'] = self.post_user
#         return context

class PostList(generic.ListView):
    model = models.Post
    select_related = ('user', 'group')
    context_object_name = 'posts'


# class PostDetail(SelectRelatedMixin, generic.DetailView):
#     model = models.Post
#     select_related = ('user', 'group')
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')


class PostUpdate(SelectRelatedMixin, generic.UpdateView, LoginRequiredMixin):
    model = models.Post
    form_class = forms.PostForm
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Post
    form_class = forms.PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)
