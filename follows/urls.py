from django.contrib import admin
from django.urls import path,include
from rede_social import views
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login_user'),
    path('login/submit', views.submit_login, name='submit'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('',RedirectView.as_view(url='index')),
    path('index/todos/', views.todos, name='todos'),
    path('index/comentar/',views.publicar, name='publicar'),
    path('index/comentarios/', views.comentarios, name='comentarios'),
    path('index/amigos/', views.amigos, name="amigos")
]
