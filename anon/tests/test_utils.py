# stdlib
import itertools
import random

# django
from django.test import TestCase

# deps
import mock

# local
from .. import utils


class UtilsTestCase(TestCase):
    def setUp(self):
        utils._word_generator = itertools.cycle(utils.WORD_LIST)
        utils._number_generator = itertools.cycle('123456789')

    def test_fake_word(self):
        text = utils.fake_word(min_size=6)
        expected = 'accusamus'
        self.assertEqual(text, expected)

    def test_fake_text(self):
        text = utils.fake_text(40)
        expected = 'a ab accusamus accusantium ad adipisci'
        self.assertEqual(text, expected)

    def test_fake_text_separator(self):
        text = utils.fake_text(40, separator='...')
        expected = 'a...ab...accusamus...accusantium...ad'
        self.assertEqual(text, expected)

    def test_fake_name(self):
        text = utils.fake_name(15)
        expected = 'A Ab Accusamus'
        self.assertEqual(text, expected)

    @mock.patch("random.randint")
    def test_fake_username(self, mock_randint):
        mock_randint.return_value = 135229
        text = utils.fake_username(15, separator='_')
        expected = 'a_ab_ad135229'
        self.assertEqual(text, expected)

    @mock.patch("random.randint")
    def test_fake_email(self, mock_randint):
        mock_randint.return_value = 135229
        text = utils.fake_email(20)
        expected = 'a135229@example.com'
        self.assertEqual(text, expected)

    def test_fake_url(self):
        text = utils.fake_url(30, scheme='https://', suffix='.com.br')
        expected = 'https://a.ab.accusamus.com.br'
        self.assertEqual(text, expected)

    def test_fake_phone_number(self):
        text = utils.fake_phone_number(format='(99) 9999-9999')
        expected = '(12) 3456-7891'
        self.assertEqual(text, expected)
