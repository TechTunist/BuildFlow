from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase


"""
Define the test cases as subclasses of the TestCase class.
Each test case should define one or more test methods that perform assertions on the app components
"""

class UserCreationTest(TestCase):

    def test_create_user_form_is_valid(self):
        """Test to create a new user with standard form data."""

        test_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

        form = UserCreationForm(data=test_data)

        # validate form, save form and test new user instance
        self.assertTrue(form.is_valid())
        

    def test_create_new_user(self):
        """Test to create a new user with standard form data."""

        user = User.objects.create_user(
            username='Testuser2',
            email='test2@gmail.com',
            password='password2')
        
        self.assertEqual(user.email, 'test2@gmail.com')
        

        
