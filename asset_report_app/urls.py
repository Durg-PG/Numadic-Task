from django.urls import path
from . import views

urlpatterns = [
    path('generate_asset_report/<int:start_time>/<int:end_time>/', views.generate_asset_report, name='generate_asset_report'),
]