from django.urls import path
from . import views

urlpatterns = [
    # With function-based view we can handle all of
    # CREATE, READ( Both Detail and List Views), UPDATE, DELETE
    # requests with just using only 2 endpoints.
    path('items/', views.CRUDView),
    path('items/<int:pk>', views.CRUDView)
]