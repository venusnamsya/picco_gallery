# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('', views.homepage, name='homepage'),
#     path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
#     path('photo/<int:pk>/like/', views.like_photo, name='like_photo'),
#     path('photo/<int:pk>/dislike/', views.dislike_photo, name='dislike_photo'),
#     path('register/', views.register_view, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='photo_gallery/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
#     path('profile/', views.profile_view, name='profile'),
# ]
