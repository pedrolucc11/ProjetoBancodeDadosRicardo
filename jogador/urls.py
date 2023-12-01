from rest_framework import routers 
from .views import JogViewset

# Criação das Routes para que as vizualizações sejam possíveis para ambas as entidades

router = routers.DefaultRouter()
router.register(r'jogador', JogViewset, basename="Jogador")

urlpatterns = router.urls