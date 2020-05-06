from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):
	'''
	 Saves new entry in database
	'''
	if request.method == 'POST':
		form = NewPlaceForm(request.POST)
		place = form.save()
		if form.is_valid():
			place.save()
			return redirect('place_list')

	'''
	 Shows non-visited places on homepage, and the fields from form.py
	'''
	places = Place.objects.filter(visited=False).order_by('name')
	new_place_form = NewPlaceForm()
	return render(request, 'travel_wishlist/wishlist.html', { 'places': places, 'new_place_form': new_place_form })

def places_visited(request):
	'''
	 Shows visited places on secondary page
	'''
	visited = Place.objects.filter(visited=True).order_by('name')
	return render(request, 'travel_wishlist/visited.html', { 'visited': visited })

def place_was_visited(request, place_pk):
	'''
	 Update entry in database to visited
	'''
	if request.method == 'POST':
		place = get_object_or_404(Place, pk=place_pk)
		place.visited = True
		place.save()

	return redirect('place_list')
