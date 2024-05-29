from unittest import TestCase

from main import TestApp


class TestTestApp(TestCase):
    app = TestApp()

    def test_print_name(self):
        self.assertEqual(self.app.name, "Fedor")
