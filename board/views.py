from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .models import Post, Category, Comment
from .forms import CommentForm
from django.core.exceptions import PermissionDenied


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/board/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_superuser or request.user == self.get_object().author):
            return super(PostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'content', 'file_upload']
    template_name = 'board/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_superuser or request.user == self.get_object().author):
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'file_upload']

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/board/')


class PostList(ListView):
    model = Post
    ordering = '-created_at'
    ordering_state = True

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        order = self.request.GET.get('ordering', '-created_at')
        return Post.objects.all().order_by(order)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['comment_form'] = CommentForm
        return context

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

    return render(
        request,
        'board/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'category': category,
        }
    )
