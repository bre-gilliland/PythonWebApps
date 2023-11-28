from django.contrib import admin 
from django.urls import path 
from blog.views import 

urls patterns = [
    # Article 
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/<init:pk>", ArticleDetailView.as_view(), name="Article_detail"),
    path("article/add", ArticleCreateView.as_view(), name="article_add"),
    path("aritlce/<init:pk/>", ArticleUpdateView(), name="article_edit",
    path("article/<init:pk/detete", ArticleDetleteView.as_view(), name="article_delete")
]