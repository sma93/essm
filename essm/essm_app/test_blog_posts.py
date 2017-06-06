import unittest
import sdbee

class TestBlogPosts(unittest.TestCase):
	def setUp(self):
		self.meta = sdbee.sdb_blog_posts()

	def test_blog_posts_metadata_contains_number_of_items(self):
		self.assertTrue(self.meta.has_key('ItemCount'))

	def test_blog_posts_metadata_contains_number_of_attributes(self):
		self.assertTrue(self.meta.has_key('AttributeNameCount'))
	
	#def blog_posts_can_be_saved(self):


	#def blog_posts_can_be_retrieved(self):

	#def blog_posts_can_be_deleted(self):

	#def blog_posts_can_be_edited(self):

if __name__ == '__main__':
	unittest.main()
