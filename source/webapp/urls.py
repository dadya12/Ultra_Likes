from django.urls import path
from django.views.generic import RedirectView

from webapp.views import UpdateArticleView, DeleteArticleView, ArticleListView, CreateArticleView, \
    ArticleDetailView, CreateCommentView, UpdateCommentView, DeleteCommentView
from webapp.views.articles import LikeArticleView
from webapp.views.comments import LikeCommentView
app_name = 'webapp'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('', RedirectView.as_view(pattern_name='webapp:articles')),
    path('create/', CreateArticleView.as_view(), name='create_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', UpdateArticleView.as_view(), name='update_article'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(), name='delete_article'),
    path('article/<int:pk>/comment/create/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    path('article/<int:pk>/like/', LikeArticleView.as_view(), name='article_like'),
    path('comment/<int:pk>/like/', LikeCommentView.as_view(), name='comment_like'),
]
