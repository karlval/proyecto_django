from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    #   as_view() es una funcion que nos permite crear una vista basada en una clase
    #   name es el nombre de la vista en la navegación
    path('', HomeView.as_view(), name = "home"),
    path('blog/', include('blog.urls', namespace="blog")),
]
