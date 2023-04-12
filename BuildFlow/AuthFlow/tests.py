from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy


# Define the test cases as subclasses of the TestCase class.
# Each test case should define one or more test methods that perform assertions on the app components


class UserCreationTest(TestCase):

    def test_create_user_form_is_valid(self):
        """Test to check if the form is valid."""

        test_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

        form = UserCreationForm(data=test_data)

        # validate form, save form and test new user instance
        self.assertTrue(form.is_valid())

    def test_create_custom_user_form_is_valid(self):
        """Test to check if the custom user form is valid."""

        test_data = {
            'username': 'testuser2',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

        form = CustomUserCreationForm(data=test_data)

        # validate form, save form and test new user instance
        self.assertTrue(form.is_valid())

    def test_create_custom_user(self):
        """Test to check if we can create a user from the custom form."""

        test_data = {
            'username': 'testuser3',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

        form = CustomUserCreationForm(data=test_data)
        self.assertTrue(form.is_valid())
        user = form.save()

        # validate form, save form and test new user instance
        self.assertEqual(user.username, 'testuser3')
        self.assertEqual(user.email, 'testuser@example.com')
        

    def test_create_new_user(self):
        """Test to create a new user with standard form data."""

        user = User.objects.create_user(
            username='Testuser4',
            email='test2@gmail.com',
            password='password2')
        
        self.assertEqual(user.username, 'Testuser4')
        self.assertEqual(user.email, 'test2@gmail.com')


class SignupViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('authflow:signup')

    def test_signup_page_renders_correctly(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authflow/signup.html')
        

    def test_signup_success(self):

        data = {
            'username': 'testuser5',
            'email': 'testuser@example.com',
            'password1': '1234rret',
            'password2': '1234rret'
        }

        response = self.client.post(self.url, data)
        self.assertTrue(User.objects.filter(username='testuser5').exists())

    def test_signup_failure(self):

        data = {
            'username': 'testuser6',
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'testpassword2'
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authflow/signup.html')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')
        self.assertFalse(User.objects.filter(username='testuser6').exists())

        

        
