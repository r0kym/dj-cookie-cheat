"""
URLconf of the cheat page
"""


from django.urls import path

from . import views


urlpatterns = [
    path('', views.cheat, name='cheat'),
]
