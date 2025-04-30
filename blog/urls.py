from django.urls import path
# . means current folder
from . import views
from .views import SignUpView

urlpatterns = [
    #path that takes in 3 arguments - path url (/pagename), function you want to run when you go to the url, and if you want to create a separate name for the function that the view can use
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('logout/', views.logout_view, name='logout')
]