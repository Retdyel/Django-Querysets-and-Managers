from django.urls import path
from . import views 

app_name="link"

urlpatterns = [
    path("create/", views.PostCreateAPI.as_view(), name="api_create"),
    path("update/<int:pk>", views.PostUpdateAPI.as_view(), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteAPI.as_view(), name="api_delete"),
    path("", views.PostListAPI.as_view(), name="api_list"),
    path("active/", views.ActiveLinkView.as_view(), name='active_link'),
    path("recent/", views.RecentLinkView.as_view(), name='recent_link'),
]