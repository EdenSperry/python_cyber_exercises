import unittest

from Solutions.level1 import validate_email


class Level1TestCase(unittest.TestCase):

    def test_valid_emails(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name+tag+sorting@example.com"))
        self.assertTrue(validate_email("x@example.com"))
        self.assertTrue(validate_email("example-indeed@strange-example.com"))
        self.assertTrue(validate_email("example@s.solutions"))
        self.assertTrue(validate_email("username@-example.com"))
        self.assertTrue(validate_email("username@111.222.333.44444"))

    def test_invalid_emails(self):
        self.assertFalse(validate_email("plainaddress"))
        self.assertFalse(validate_email("@missingusername.com"))
        self.assertFalse(validate_email("username@.com"))
        self.assertFalse(validate_email("username@com"))
        self.assertFalse(validate_email("admin@mailserver1"))
        self.assertFalse(validate_email("username@."))
        self.assertFalse(validate_email("username@..com"))
        self.assertFalse(validate_email("user@[IPv6:2001:db8::1]"))


if __name__ == '__main__':
    unittest.main()
