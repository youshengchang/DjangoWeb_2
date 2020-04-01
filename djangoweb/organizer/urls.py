from django.urls import path

#from .views import tag_detail, tag_list

from .views import (
    TagList,
    TagDetail,
    TagDelete,
    TagUpdate,
    TagCreate,
    StartupList,
    StartupDetail,
    StartupCreate,
    StartupDelete,
    StartupUpdate,
    )


urlpatterns = [
    #path("tag/", tag_list, name="tag_list"),
    #path("tag/<str:slug>/",tag_detail,name="tag_detail"),
    path("tag/", TagList.as_view(), name="tag_list"),
    path("tag/<str:slug>/",TagDetail.as_view(),name="tag_detail"),
    path("tag/create", TagCreate.as_view(), name="tag_create"),
    path("tag/<str:slug>/update/", TagUpdate.as_view(),name="tag_update"),
    path("tag/<str:slug>/delete/",TagDelete.as_view(),name="tag_delete"),
    path("startup/", StartupList.as_view(), name="startup_list"),
    path("startup/create/",StartupCreate.as_view(),name="startup_create"),
    path("startup/<str:slug>/",StartupDetail.as_view(),name="startup_detail"),
    path("startup/<str:slug>/delete/",StartupDelete.as_view(),name="startup_delete"),
    path("startup/<str:slug>/update/",StartupUpdate.as_view(),name="startup_update"),
]
