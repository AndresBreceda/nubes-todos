from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Rutas de Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Rutas del Sistema
    path('dashboard/', views.dashboard, name='dashboard'),
    path('curso/<int:curso_id>/calificaciones/', views.grade_entry, name='grade_entry'),
    path('curso/<int:curso_id>/iniciar-firma/', views.iniciar_firma, name='iniciar_firma'),
    path('curso/<int:curso_id>/firmar/', views.digital_signature, name='digital_signature'),
    path('curso/<int:curso_id>/pdf/', views.generar_pdf, name='generar_pdf'),
]