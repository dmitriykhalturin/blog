from django.urls import path

from .views import ArticleListView, ArticleDetailView

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
