from django.test import TestCase
from .forms import CommentForm

# Create your tests here.

class TestCommentForm(TestCase):
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'd'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': 'g'})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')
