from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    TagAPIList,
    TagAPIDetail,
    StartupAPIList,
    StartupAPIDetail,
    NewsLinkAPIList,
    NewsLinkAPIDetail,
    )
from .viewsets import TagViewSet, StartupViewSet, NewsLinkViewSet

class NewsLinkRouter(SimpleRouter):
    """Override the SimpleRouter for articles

    DRF's routers expect there to only be a single variable
    for finding objects. However, our NewsLinks needs
    two! We therefore override the Router's behavior to
    make it do what we want.

    The big question: was it worth switching to a ViewSet
    and Router over our previous config for this?
    """

    def get_lookup_regex(self, *args, **kwargs):
        """Return regular expression pattern for URL path

        This is the (rough) equivalent of the simple path:
            <str:startup_slug>/<str:newslink_slug>
        """
        return (
            r"(?P<startup_slug>[^/.]+)/"
            r"(?P<newslink_slug>[^/.]+)"
        )


api_router = SimpleRouter()
api_router.register("tag", TagViewSet, basename="api-tag")
api_router.register("startup", StartupViewSet, basename="api-startup")
api_routers = api_router.urls

nl_router = NewsLinkRouter()
nl_router.register(
    "newslink", NewsLinkViewSet, basename="api-newslink"
)

urlpatterns = api_router.urls + nl_router.urls

'''
urlpatterns = api_routers + [
    #path("tag/", TagAPIList.as_view(), name="api-tag-list"),
    #path("tag/<str:slug>/", TagAPIDetail.as_view(),name="api-tag-detail"),
    #path("startup/", StartupAPIList.as_view(), name="api-startup-list"),
    #path("startup/<str:slug>/", StartupAPIDetail.as_view(), name="api-startup-detail"),
    path("newslink/",NewsLinkAPIList.as_view(),name="api-newslink-list"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>/", NewsLinkAPIDetail.as_view(),name="api-newslink-detail")
]
'''
