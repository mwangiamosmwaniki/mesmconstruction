from django.urls import path
from .views import home, cyber_services, entertainment, graphics_design, construction, contact,add_review
from services import views

urlpatterns = [
    path('', home, name='home'),
    path('cyber-services/', cyber_services, name='cyber_services'),
    path('entertainment/', entertainment, name='entertainment'),
    path('graphics-design/', graphics_design, name='graphics_design'),
    path('construction/', construction, name='construction'),
    path('contact/', contact, name='contact'),
    path('add-review/', add_review, name='add_review'),
    path('category/<str:category_name>/', views.category_images, name='category_images'),
]
