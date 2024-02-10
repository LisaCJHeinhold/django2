from .import views
from django.urls import path

# url patters for post details
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),  # Update this line
]