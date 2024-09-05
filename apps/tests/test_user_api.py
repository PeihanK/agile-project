from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.users.models import User

# создание новых пользователей
class UserAPITests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='password_john',
            first_name='John',
            last_name='Doe',
            email='john@example.com'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='password_jack',
            first_name='Jack',
            last_name='Sparrow',
            email='jack@example.com'
        )

    def test_get_all_users(self):
        # получение всех пользователей
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # ожидаем 2 пользователя

    def test_register_new_user(self):
        # регистрация нового пользователя
        user_data = {
            'username': 'user3',
            'first_name': 'Bill',
            'last_name': 'Gates',
            'email': 'bill@example.com',
            'position': 'CEO',
            'password': 'password_bill',
            're_password': 'password_bill',
        }
        response = self.client.post(reverse('user-register'), user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)  # ожидаем 3 пользователя

    def test_registration_passwords_dont_match(self):
        # ошибки валидации при несовпадении паролей
        user_data = {
            'username': 'user4',
            'first_name': 'Ilon',
            'last_name': 'Mask',
            'email': 'ilon@example.com',
            'position': 'CTO',
            'password': 'password_ilon',
            're_password': 'ilon_password',
        }
        response = self.client.post(reverse('user-register'), user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)  # ошибка пароля
