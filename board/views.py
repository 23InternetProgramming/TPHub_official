from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category
from django.core.exceptions import PermissionDenied

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/board/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'content', 'file_upload']
    template_name = 'board/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'file_upload']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/board/')

class PostList(ListView) :
    model = Post
    ordering = '-pk'
    ordering_state = True

    def change_ordering(self):
        self.ordering = 'pk' if self.ordering_state else '-pk'
        self.ordering_state = not self.ordering_state

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

    # 현재 로그인 유저와 글쓴 유저가 같다면.. -> 글수정, 삭제 버튼 보이기
    def user_valid(self):
        current_user = self.request.user
        if current_user == self.object.auth:
            return True
        else:
            return False

class CategoryList(ListView):
    model = Category
    ordering = ['name']

def category_post(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category)

    return render (
        request,
        '/board/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'category' : category,
        }
    )
