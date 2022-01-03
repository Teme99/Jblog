from django.urls import path, include
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('category/<str:cats>', CategoryView, name="category"),
    path('article/<int:pk>/delete', ArticleDetailView.as_view(), name="articleDetail"),
]
