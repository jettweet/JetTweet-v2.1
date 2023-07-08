from django.urls import path
from .views import (
	home,
	PostDetail,
	category,
	CreateArticle,
	ListArticle,
	ArticleUpdate,
	ArticleDeleteView,
	)
urlpatterns = [
	path('',home,name="home"),
	path('<int:pk>/',PostDetail.as_view(),name='detail'),
	path('category/<slug:slug>/',category,name='category'),
	path('list/',ListArticle.as_view(),name="list"),
    path('create/',CreateArticle.as_view(),name='create'),
    path('update/<int:pk>/',ArticleUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',ArticleDeleteView.as_view(),name="delete")

]