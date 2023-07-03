from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)

urlpatterns=[
    #path("",views.index, name="index"),
    # path("categorias/", views.categorias,name="categorias"),
    path("",include(router.urls)),
]