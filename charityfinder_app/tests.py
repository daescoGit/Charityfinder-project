from django.test import TestCase
from django.contrib.auth.models import User

from . models import Comment


class CommentTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        # Create a comment
        test_comment = Comment.objects.create(
            author=testuser1, body='Body content...'
        )
        test_comment.save()

    def test_content(self):
        post = Comment.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_body, 'Body content...')
