from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

# Create your tests here.
class TestAboutView(TestCase):

    def setUp(self):
        """ Creates about me content"""
        self.about_content = About(title="title",
                        content='content',)


    def test_render_about_page_with_collab_form(self):
        """Verifies get request for about me containing collab form"""
        response = self.client.get(reverse(
            "about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"content", response.content)
        self.assertIn(b"title", response.content)
        self.assertIsInstance(response.context["collaborate_form"], CollaborateForm)

    def test_collab_form_post_success(self):
        "Test for a user requesting a collaboration"
        post_data = {'name': 'Jamie',
                    'email': 'j@g.com',
                    'message': 'g'}
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Collaboration request received! I endeavour to respond within 2 working days.", response.content)



