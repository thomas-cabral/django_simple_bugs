"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from .simple_bugs.models import Case


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class CaseTest(TestCase):
    def setUp(self):
        Case.objects.create(type='BUG', title='Case Test 1', detail='some data', closed=False)
        Case.objects.create(type='FEATURE_REQUEST', title='Case Test 2', detail='some more data', closed=False)