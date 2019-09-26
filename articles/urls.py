from django.urls import path
from . import views

app_name = 'articles'
# www.domain.com/articles/___
urlpatterns = [  # articles:name
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
]
