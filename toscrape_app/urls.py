from django.urls import path
from . import views

app_name = 'toscrape_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('quotes/', views.quote, name='quotes'),
    path('authors/', views.author, name='authors'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('tags/<str:tag>/', views.tag_quotes, name='tag_quotes'),
]