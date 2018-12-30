import unittest

from mock import patch, Mock

from app.core.models import Translation
from app.tasks import send_translation_to_unbabel


class TestTask(unittest.TestCase):

    @patch('app.tasks.update_translation')
    @patch('app.tasks.send_request_to_unbabel')
    @patch('app.create_app')
    def test_send_translation_to_unbabel_wrong(self,
                                               mock_create_app,
                                               mock_send_request_to_unbabel,
                                               mock_update_translation):

        mock_create_app.return_value.app_context.return_value = True
        mock_send_request_to_unbabel.return_value = Mock()
        mock_send_request_to_unbabel.return_value.status_code = 400

        send_translation_to_unbabel('uid', 'This is a test')

        mock_update_translation.assert_called_with('uid', status=Translation.CANCELLED)

    @patch('app.tasks.update_translation')
    @patch('app.tasks.send_request_to_unbabel')
    @patch('app.create_app')
    def test_send_translation_to_unbabel_no_response(self,
                                                     mock_create_app,
                                                     mock_send_request_to_unbabel,
                                                     mock_update_translation):

        mock_create_app.return_value.app_context.return_value = True
        mock_send_request_to_unbabel.return_value = Mock()
        mock_send_request_to_unbabel.return_value = None

        send_translation_to_unbabel('uid', 'This is a test')

        mock_update_translation.assert_called_with('uid', status=Translation.CANCELLED)

    @patch('app.tasks.update_translation')
    @patch('app.tasks.send_request_to_unbabel')
    @patch('app.create_app')
    def test_send_translation_to_unbabel_right(self,
                                               mock_create_app,
                                               mock_send_request_to_unbabel,
                                               mock_update_translation):

        mock_create_app.return_value.app_context.return_value = True
        mock_send_request_to_unbabel.return_value = Mock()
        mock_send_request_to_unbabel.return_value.status_code = 201

        send_translation_to_unbabel('uid', 'This is a test')

        mock_update_translation.assert_called_with('uid', status=Translation.PENDING)
