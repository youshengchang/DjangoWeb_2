from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )

from .models import Post
from .serializers import PostSerializer
from .forms import PostForm

class PostList(ListView):
    model = Post
    template_name = "post/list.html"

class PostDetail(DetailView):
    queryset = Post.objects.all()
    template_name = "post/detail.html"

'''
    def get(self, request, year,month, slug):
        post = get_object_or_404(Post, pub_date__year = year, pub_date__month=month,slug=slug,)
        return render(request, "post/detail.html",{"post":post})
'''
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = "post/form.html"
    extra_context = {"update": False}
    success_url = reverse_lazy("post_list")

class PostDelete(DeleteView):
    """Confirm and delete a Post via HTML Form"""

    model = Post
    template_name = "post/confirm_delete.html"
    success_url = reverse_lazy("post_list")


class PostUpdate(UpdateView):
    """Update a Post via HTML form"""

    form_class = PostForm
    model = Post
    template_name = "post/form.html"
    extra_context = {"update": True}


class PostAPIList(ListAPIView):
    print("PostAPIList get called.")
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostAPIDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        month = self.kwargs.get("month")
        year = self.kwargs.egt("year")
        slug = self.kwargs.get("slug")

        queryset = self.filter_queryset(self.get_queryset())

        post = get_object_or_404(
            queryset,
            pub_date__year = year,
            pub_date__month = month,
            slug = slug,

        )
        self.check_object_permissions(self.request, post)
        return post
