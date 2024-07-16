from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2OperationalError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('django.core.management.base.BaseCommand.check')
class CommandTest(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if database ready"""
        # Mock the check method to return True
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep', return_value=None)
    @patch('django.core.management.base.BaseCommand.check')
    def test_wait_for_db_delay(self, patched_check, patched_sleep):
        """Test waiting for db when getting OperationalError"""
        # Side effects: raise errors, then succeed
        side_effects = [
            psycopg2OperationalError] * 2 + [
            OperationalError] * 3 + [
            True
        ]
        patched_check.side_effect = side_effects

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
