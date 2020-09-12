from django.urls import path
from .views import groups, not_joined, join_group, detail_group_user, detail_group_wordwall, create_post, list_posts, detail_post

app_name = 'share'

urlpatterns = [
    path('groups', groups, name='groups'),
    path('notjoined', not_joined, name='not_joined'),
    path('join/<int:pk>', join_group, name='join_group'),
    path('detail/users/<int:pk>', detail_group_user, name='detail_group_user'),
    path('detail/wordwall/<int:pk>', detail_group_wordwall, name='detail_group_wordwall'),
    path('post/create/<int:pk>', create_post, name="create_post"),
    path('post/listings/<int:pk>', list_posts, name="list_posts"),
    path('post/detail/<int:pk>', detail_post, name="detail_post"),
]



