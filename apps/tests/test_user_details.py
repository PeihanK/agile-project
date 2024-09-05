from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.projects.models import Project
from apps.users.models import User


class UserDetailAPITests(APITestCase):
	def setUp(self):
		# cоздание нового пользователя
		self.user = User.objects.create_user(
			username='user1',
			password='password_john',
			first_name='John',
			last_name='Doe',
			email='john@example.com',
			phone='123456789',
			position='Developer',
			project=Project.objects.create(name='John Doe Project')
		)

	def test_get_user_by_id(self):
		# получение информации по ID
		response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['username'], self.user.username)
		self.assertEqual(response.data['first_name'], self.user.first_name)
		self.assertEqual(response.data['email'], self.user.email)

	def test_get_non_existent_user(self):
		# получение пользователя с несуществующим ID
		response = self.client.get(reverse('user-detail', kwargs={'pk': 999}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		self.assertIn('detail', response.data)
