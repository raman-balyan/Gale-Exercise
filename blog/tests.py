from django.test import TestCase
from models import Blog

class BlogTests(TestCase):
	def test_str(self):
		my_title = Blog(title='Title for a test case')
		self.assertEquals(
			str(my_title), 'Title for a test case',
			)

