from unittest import TestCase

from mock import patch, Mock

from app.core.models import Translation
from app.core.utils import translation_uuid_exists, generate_uuid, store_translation_in_database, update_translation, \
    get_translations


class UtilsTest(TestCase):

    @patch('app.core.utils.db')
    def test_translation_uuid_exists(self, mock_db):
        mock_db.session.query.return_value.filter.return_value.first.return_value = Mock(spec=Translation)
        self.assertTrue(translation_uuid_exists('some-uuid'))
        mock_db.session.query.return_value.filter.return_value.first.return_value = None
        self.assertFalse(translation_uuid_exists('some-uuid'))

    @patch('app.core.utils.generate_uuid')
    @patch('app.core.utils.translation_uuid_exists')
    def test_generate_uuid_does_not_exists(self, mock_translation_uuid_exists, mock_generate_uuid):
        mock_translation_uuid_exists.return_value = False
        generate_uuid()
        self.assertFalse(mock_generate_uuid.called)

    @patch('app.core.utils.generate_uuid')
    @patch('app.core.utils.translation_uuid_exists')
    def test_generate_uuid_does_exists(self, mock_translation_uuid_exists, mock_generate_uuid):
        mock_translation_uuid_exists.return_value = True
        mock_generate_uuid.return_value = 'some-uuid'
        uid = generate_uuid()
        self.assertEqual(uid, 'some-uuid')
        self.assertTrue(mock_generate_uuid.called)

    @patch('app.core.utils.settings')
    @patch('app.core.utils.generate_uuid')
    @patch('app.core.utils.db')
    def test_store_translation_in_database(self, mock_db, mock_generate_uuid, mock_settings):
        mock_generate_uuid.return_value = 'some-uuid'
        mock_settings.SOURCE_TRANSLATION_LANGUAGE = 'en'
        mock_settings.TARGET_TRANSLATION_LANGUAGE = 'es'
        mock_db.session.add.return_value = None
        mock_db.session.commit.return_value = None
        translation = store_translation_in_database('SOME TEXT')

        self.assertEqual(translation.source_text, 'SOME TEXT')
        self.assertEqual(translation.source_language, 'en')
        self.assertEqual(translation.target_language, 'es')
        self.assertEqual(translation.uuid, 'some-uuid')

    @patch('app.core.utils.translation_uuid_exists')
    @patch('app.core.utils.db')
    def test_update_translation_uid_does_not_exists(self, mock_db, mock_translation_uuid_exists):
        mock_translation_uuid_exists.return_value = False
        mock_db.session.query.return_value.filter.return_value = Mock()
        mock_db.session.query.return_value.filter.return_value.update.return_value = "SOME QUERY"
        mock_db.session.commit.return_value = None
        mock_db.session.flush.return_value = None

        update_translation('some-uuid', status=Translation.PENDING)

        self.assertFalse(mock_db.session.query.return_value.filter.return_value.update.called)

    @patch('app.core.utils.translation_uuid_exists')
    @patch('app.core.utils.db')
    def test_update_translation_status(self, mock_db, mock_translation_uuid_exists):
        mock_translation_uuid_exists.return_value = True
        mock_db.session.query.return_value.filter.return_value = Mock()
        mock_db.session.query.return_value.filter.return_value.update.return_value = "SOME QUERY"
        mock_db.session.commit.return_value = None
        mock_db.session.flush.return_value = None

        update_translation('some-uuid', status=Translation.PENDING)

        mock_db.session.query.return_value.filter.return_value.update.assert_called_with({'status': Translation.PENDING})

    @patch('app.core.utils.translation_uuid_exists')
    @patch('app.core.utils.db')
    def test_update_translation_translated_text(self, mock_db, mock_translation_uuid_exists):
        mock_translation_uuid_exists.return_value = True
        mock_db.session.query.return_value.filter.return_value = Mock()
        mock_db.session.query.return_value.filter.return_value.update.return_value = "SOME QUERY"
        mock_db.session.commit.return_value = None
        mock_db.session.flush.return_value = None

        update_translation('some-uuid', translated_text="SOME TRANSLATION")

        mock_db.session.query.return_value.filter.return_value.update.assert_called_with(
            {'translated_text': "SOME TRANSLATION"})

    @patch('app.core.utils.desc')
    @patch('app.core.utils.db')
    def test_get_translations_with_ascend(self, mock_db, mock_desc):
        mock_db.session.query.return_value.order_by.return_value.all.return_value = [
            Translation(uuid='uuid3', source_text='some text 3', source_language='en', target_language='es', status=Translation.PENDING),
            Translation(uuid='uuid1', source_text='some text', source_language='en', target_language='es', status=Translation.PENDING),
        ]
        result = get_translations()
        self.assertEqual(result[0]['uuid'], 'uuid3')
        self.assertEqual(result[0]['source_text'], 'some text 3')
        self.assertEqual(result[0]['source_language'], 'en')
        self.assertEqual(result[0]['target_language'], 'es')
        self.assertEqual(result[0]['status'], 'PENDING')

        self.assertEqual(result[1]['uuid'], 'uuid1')
        self.assertEqual(result[1]['source_text'], 'some text')
        self.assertEqual(result[1]['source_language'], 'en')
        self.assertEqual(result[1]['target_language'], 'es')
        self.assertEqual(result[1]['status'], 'PENDING')

        mock_desc.assert_not_called()

    @patch('app.core.utils.desc')
    @patch('app.core.utils.db')
    def test_get_translations_with_descend(self, mock_db, mock_desc):
        mock_db.session.query.return_value.order_by.return_value.all.return_value = [
            Translation(uuid='uuid1', source_text='some text', source_language='en', target_language='es', status=Translation.PENDING),
            Translation(uuid='uuid3', source_text='some text 3', source_language='en', target_language='es', status=Translation.PENDING),
        ]
        get_translations(descend=True)

        mock_desc.assert_called()