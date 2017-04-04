"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
import json
from web.views import process_filters
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        django.setup()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class GroupingTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        django.setup()
    
    def test_process_filters(self):
        self.maxDiff = None
        json_str = '{"type":"grouping-configuration","name":"Placeholder Grouping","floors":[{"name":"Floor 1","groups":[{"name":"Group 1","wards":[{"name":"Ward 1","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]},{"name":"Ward 2","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]}]},{"name":"Group 2","wards":[{"name":"Ward 1","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]},{"name":"Ward 2","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]}]}]},{"name":"Floor 2","groups":[{"name":"Group 1","wards":[{"name":"Ward 1","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]},{"name":"Ward 2","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]}]},{"name":"Group 2","wards":[{"name":"Ward 1","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]},{"name":"Ward 2","boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}]}]}]}]}'
        json_obj = json.loads(json_str)
        process_filters(json_obj)
        self.assertEqual(json.loads(json.dumps(json_obj)), json.loads('{"floors":[{"selected":true,"name":"Floor 1","groups":[{"selected":true,"wards":[{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 1"},{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 2"}],"name":"Group 1"},{"selected":true,"wards":[{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 1"},{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 2"}],"name":"Group 2"}]},{"selected":true,"name":"Floor 2","groups":[{"selected":true,"wards":[{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 1"},{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 2"}],"name":"Group 1"},{"selected":true,"wards":[{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 1"},{"boxes":[{"name":"Box 1","address":"1A2B3C4D5E6F"},{"name":"Box 2","address":"1A2B3C4D5E6F"},{"name":"Box 3","address":"1A2B3C4D5E6F"}],"selected":true,"name":"Ward 2"}],"name":"Group 2"}]}],"type":"grouping-configuration","name":"Placeholder Grouping"}'))
    