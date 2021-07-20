# stdlib
from mock import patch
import re
from signal import SIGALRM, alarm, signal

# deps
from django.test import TestCase

# local
from anon import utils


class UtilsTestCase(TestCase):
    def test_fake_word(self):
        text = utils.fake_word(min_size=6)
        self.assertGreaterEqual(len(text), 6)

    def test_fake_text(self):
        text = utils.fake_text(40)
        self.assertLessEqual(len(text), 40)

    def test_fake_text_separator(self):
        text = utils.fake_text(40, separator="...")
        self.assertIn("...", text)

    def test_fake_name(self):
        text = utils.fake_name(15)
        self.assertLessEqual(len(text), 15)

    def test_fake_username(self):
        text = utils.fake_username(45, separator="_")
        self.assertIn("_", text)
        self.assertLessEqual(len(text), 45)

    @patch('anon.utils._word_generator', ["placeholder"])
    def test_fake_username_duration(self):
        method = utils.fake_username
        timeout_seconds = 1

        def timeout_handler(signum, frame):
            raise RuntimeError(
                "{} method call exceeded {} second timeout".format(
                    method.__name__,
                    timeout_seconds
                )
            )

        signal(SIGALRM, timeout_handler)
        alarm(timeout_seconds)

        method(max_size=10)

    def test_fake_email(self):
        text = utils.fake_email(20)
        self.assertLessEqual(len(text), 20)

    def test_fake_url(self):
        text = utils.fake_url(30, scheme="https://", suffix=".com.br")
        self.assertLessEqual(len(text), 30)
        self.assertTrue(text.startswith("https://"))
        self.assertIn(".com.br", text)

    def test_fake_phone_number(self):
        text = utils.fake_phone_number(format="(99) 9999-9999")
        self.assertTrue(bool(re.match(r"^\(\d{2}\) \d{4}-\d{4}$", text)))
