from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestHomePageIsEmptyList(TestCase):

	def test_load_home_page_shows_empty_list(self):
		response = self.client.get(reverse('place_list'))
		self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
		self.assertFalse(response.context['places'])
		self.assertContains(response, 'You have no places in your wishlist')


class TestVisitedPageIsEmptyList(TestCase):

	def test_no_places_visited_message(self):
		response = self.client.get(reverse('places_visited'))
		self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
		self.assertFalse(response.context['visited'])
		self.assertContains(response, 'You have not visited any places yet.')

class TestWishList(TestCase):
	fixtures = ['test_places']

	def test_view_wishlist_contains_not_visited_places(self):
		response = self.client.get(reverse('place_list'))
		self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
		self.assertContains(response, 'Tokyo')
		self.assertContains(response, 'New York')
		self.assertNotContains(response, 'San Francisco')
		self.assertNotContains(response, 'Moab')


class TestVisited(TestCase):
	fixtures = ['test_places']

	def test_view_visited_contains_only_visited_places(self):
		response = self.client.get(reverse('places_visited'))
		self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
		self.assertContains(response, 'San Francisco')
		self.assertContains(response, 'Moab')
		self.assertNotContains(response, 'Tokyo')
		self.assertNotContains(response, 'New York')


class TestAddNewPlace(TestCase):

	def test_add_new_unvisited_place_to_wishlist(self):
		response = self.client.post(reverse('place_list'), { 'name': 'Tokyo', 'visited': False }, follow=True)

		self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

		response_places = response.context['places']
		self.assertEqual(len(response_places), 1)
		tokyo_response = response_places[0]
		tokyo_in_database = Place.objects.get(name='Tokyo', visited=False)
		self.assertEqual(tokyo_response, tokyo_in_database)


class TestVisitPlace(TestCase):
	fixtures = ['test_places']

	def test_visit_place(self):
		response = self.client.post(reverse('place_was_visited', args=(2,)), follow=True)

		self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
		self.assertNotContains(response, 'New York')
		new_york = Place.objects.get(pk=2)
		self.assertTrue(new_york.visited)

	def test_visit_non_existent_place(self):
		response = self.client.post(reverse('place_was_visited', args=(200,)), follow=True)
		self.assertEqual(response.status_code, 404)
