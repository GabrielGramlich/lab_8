from django.urls import path
from . import views

urlpatterns = [
	path('', views.place_list, name='place_list'),	#hompage
	path('visited', views.places_visited, name='places_visited'),	#visited page
	path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited')	#getting the primary key for place visited
]
