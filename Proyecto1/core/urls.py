from django.urls import path
from .views import Formulario
from .views import frenos
from .views import interior
from .views import motor
from .views import home
from .views import pintura
from .views import registro
from .views import ruedas
from .views import Iniciarsesion


urlpatterns = [
    path('home/', home,name="home"),
    path('registro/', registro,name="registro"),
    path('Formulario/', Formulario,name="Formulario"),
    #path('login', Iniciarsesion,name="Iniciarsesion"),
    path('ruedas/', ruedas,name="ruedas"),
    path('pintura/', pintura,name="pintura"),
    #path('Registrar', Registrar,name="Registrar"),
    path('motor/', motor,name="motor"),
    path('interior/', interior,name="interior"),
    path('frenos/', frenos,name="frenos"),
]
