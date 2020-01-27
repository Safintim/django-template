from django.urls import path, include
from app.v0.router import router as router_v0


urlpatterns = [
    path('api/v0/', include((router_v0.urls, 'app'), namespace='v0')),
]
