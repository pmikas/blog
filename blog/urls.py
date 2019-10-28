from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/pt', views.pt_cv, name='pt_cv'),
    path('cv/en', views.en_cv, name='en_cv'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('projects/ml', views.ml, name='ml'),
    path('projects/ml/diamonds', views.reg_diamonds, name='reg_diamonds'),
    path('projects/ml/digit_reco', views.clas_digit_reco, name='clas_digit_reco'),
    path('projects/ml/mushroom', views.clas_mushroom, name='clas_mushroom'),
    path('projects/cs', views.cs, name='cs'),
    path('projects/cs/mis', views.cs_mis, name='cs_mis'),
    path('projects/cs/agile', views.cs_agile, name='cs_agile'),
    path('projects/cs/tsql', views.cs_tsql, name='cs_tsql'),
    path('projects/cs/ml', views.cs_ml, name='cs_ml'),
    path('projects/cs/django', views.django, name='django'),
    path('projects/surf', views.surf, name='surf'),
]