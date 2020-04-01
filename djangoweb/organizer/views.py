import  json
from django.views.decorators.http import (
    require_http_methods
)
from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse, reverse_lazy

from .serializers import (
    TagSerializer,
    StartupSerializer,
    NewsLinkSerializer,
    )
from .models import Tag, Startup,NewsLink



from rest_framework.generics import  (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,

)

from django.db.models.query import QuerySet
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from django.http import HttpResponse
#from django.template import loader
from django.views.decorators.http import require_safe

from .forms import TagForm, StartupForm

class TagList(ListView):

    queryset = Tag.objects.all()
    template_name = "tag/list.html"

class TagDetail(DetailView):

    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class TagCreate(CreateView):
    print("TagCreate called.")
    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": False}
    success_url = reverse_lazy("tag_list")


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": True}


class TagDelete(DeleteView):

    model = Tag
    template_name = "tag/confirm_delete.html"
    success_url = reverse_lazy("tag_list")




class StartupList(ListView):
    queryset = Startup.objects.all()
    template_name = "startup/list.html"

class StartupDetail(DetailView):
    queryset = Startup.objects.all()
    template_name = "startup/detail.html"

class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup
    template_name = "startup/form.html"
    extra_context = {"update": False}
    success_url = reverse_lazy("startup_list")

class StartupDelete(DeleteView):
    """Confirm and delete a Startup via HTML Form"""

    model = Startup
    template_name = "startup/confirm_delete.html"
    success_url = reverse_lazy("startup_list")


class StartupUpdate(UpdateView):
    """Update a Startup via HTML form"""

    form_class = StartupForm
    model = Startup
    template_name = "startup/form.html"
    extra_context = {"update": True}



class TagAPIDetail(RetrieveUpdateDestroyAPIView):


    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagAPIList(ListCreateAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupAPIDetail(RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"

class StartupAPIList(ListAPIView):

    queryset = Startup.objects.all()

    serializer_class = StartupSerializer

class NewsLinkAPIDetail(RetrieveAPIView):

    gueryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
    print("before get_object: queryset", gueryset)

    def get_object(self):
        print("get_object() get called")
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")
        print("startup_slug: ", startup_slug, "newslink_slug: ", newslink_slug)
        queryset = self.filter_queryset(self.get_queryset())
        #print("after filter: ",queryset)
        #queryset = self.queryset
        #queryset = self.gueryset
        print("in get_object : ",queryset)
        newslink = get_object_or_404(
            queryset,
            slug = newslink_slug,
            startup__slug=startup_slug
        )
        print(newslink)
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink


class NewsLinkAPIList(ListAPIView):
    queryset = NewsLink.objects.all()
    print("newslinkapilist queryset: ",queryset)
    serializer_class = NewsLinkSerializer
