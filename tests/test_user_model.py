import unittest

from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_getter(self):
        u = User(password='test_pwd')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='test_pwd')
        self.assertTrue(u.verify_password('test_pwd'))
        self.assertFalse(u.verify_password('test_pwd1'))
        self.assertFalse(u.verify_password('test_pw'))
        self.assertFalse(u.verify_password('test_111'))

    def test_password_random(self):
        u1 = User(password='test_pwd')
        u2 = User(password='test_pwd')
        self.assertFalse(u1.password_hash == u2.password_hash)
