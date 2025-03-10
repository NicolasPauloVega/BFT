from django.urls import path
# Views
from admin_site import views

urlpatterns = [
    # Home page URL's
    path('', views.index, name='index'),
    # Graphics URL's
    path('graficos', views.charts, name='charts'),
    # User URL's
    path('usuarios', views.tables, name='tables'),
    path('iniciar-sesion', views.login, name='login'),
    path('recordar-contraseña', views.forgot_password, name='forgot-password'),
    path('registro-sesion', views.register, name='register'),
    path('cerrar-sesion', views.logout, name='logout'),
    path('actualizar-usuario/<int:id>/', views.user_update, name="user-update"),
    # Category and Subcategory URL's
    path('programa', views.category, name='category'),
    path('crear-programa', views.add_category, name="category-subcategory"),
    path('actividad/<int:categoria_id>', views.subcategory, name='subcategory-view'),
    path('crear-acividad/<int:categoria_id>', views.add_subcategory, name="subcategory"),
    # Points URL's
    path('puntos/<int:id_usuario>', views.points, name="points"),
    path('puntos/evaluar', views.save_form_points, name="form-points"),
    path('evidencias/<int:id_usuario>', views.evidence, name="evidence"),
    # Export excel
    path("exportar-excel/", views.exportar_a_excel, name="exportar_excel"),
]