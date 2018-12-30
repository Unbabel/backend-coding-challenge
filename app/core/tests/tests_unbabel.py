from unittest import TestCase

from mock import patch, Mock

from app.core.models import Translation
from app.core.unbabel import get_callback_url, send_request_to_unbabel
from app.core.utils import translation_uuid_exists, generate_uuid, store_translation_in_database, update_translation, \
    get_translations


class UnbabelTest(TestCase):

    @patch('app.core.unbabel.settings')
    def test_get_callback_url_with_ip_address(self, mock_settings):
        mock_settings.CALLBACK_IP_ADDRESS = "someaddress.com"
        self.assertEqual(get_callback_url(), "http://someaddress.com/api/translation")

    @patch('app.core.unbabel.settings')
    def test_get_callback_url_with_callback_url(self, mock_settings):
        mock_settings.CALLBACK_IP_ADDRESS = None
        mock_settings.CALLBACK_URL = "http://someaddress.com/test"
        self.assertEqual(get_callback_url(), "http://someaddress.com/test")

    @patch('app.core.unbabel.requests')
    @patch('app.core.unbabel.get_callback_url')
    @patch('app.core.unbabel.settings')
    def test_send_request_to_unbabel_right_response(self, mock_settings, mock_get_callback_url, mock_requests):
        mock_settings.UNBABEL_USERNAME = 'username'
        mock_settings.UNBABEL_PASSWORD = 'password'

        mock_settings.SOURCE_TRANSLATION_LANGUAGE = 'en'
        mock_settings.TARGET_TRANSLATION_LANGUAGE = 'es'

        mock_settings.UNBABEL_TRANSLATION_URL = "http://sandbox.unbabel.com/translation"

        mock_get_callback_url.return_value = "http://someaddress.com/test"

        mock_requests.post.return_value = "SOME OBJECT RESPONSE"

        self.assertEqual(send_request_to_unbabel('uuid-value', 'source_text'), "SOME OBJECT RESPONSE")

    @patch('app.core.unbabel.requests')
    @patch('app.core.unbabel.get_callback_url')
    @patch('app.core.unbabel.settings')
    def test_send_request_to_unbabel_wrong_response(self, mock_settings, mock_get_callback_url, mock_requests):
        mock_settings.UNBABEL_USERNAME = 'username'
        mock_settings.UNBABEL_PASSWORD = 'password'

        mock_settings.SOURCE_TRANSLATION_LANGUAGE = 'en'
        mock_settings.TARGET_TRANSLATION_LANGUAGE = 'es'

        mock_settings.UNBABEL_TRANSLATION_URL = "http://sandbox.unbabel.com/translation"

        mock_get_callback_url.return_value = "http://someaddress.com/test"

        mock_requests.post.side_effect = Exception('SOME EXCEPTION RAISE')

        self.assertEqual(send_request_to_unbabel('uuid-value', 'source_text'), None)