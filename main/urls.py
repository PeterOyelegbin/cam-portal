from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('signup/', views.registerPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<str:pk>/', views.PostDetail.as_view(), name='details'),
    path('edit/<str:pk>/', views.UpdatePost.as_view(), name='update_post'),
    path('delete/<str:pk>/', views.DeletePost.as_view(), name='delete_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
