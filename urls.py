from django.urls import path
from .views import PostsList, PostDetail, PostSearch

urlpatterns = [
    path('', PostsList.as_view(), name='posts_list'),
    path('search/', PostSearch.as_view(), name='posts_search'),
    path('<int:pk>', PostDetail.as_view(), name='posts_detail'),
]
