import unittest
from Solutions.level4 import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(encrypt("abc", 1), "bcd")
        self.assertEqual(encrypt("ABC", 1), "BCD")
        self.assertEqual(encrypt("xyz", 3), "abc")
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    def test_decrypt_basic(self):
        self.assertEqual(decrypt("bcd", 1), "abc")
        self.assertEqual(decrypt("BCD", 1), "ABC")
        self.assertEqual(decrypt("abc", 3), "xyz")
        self.assertEqual(decrypt("ABC", 3), "XYZ")

    def test_encrypt_with_non_alpha(self):
        self.assertEqual(encrypt("abc123", 1), "bcd123")
        self.assertEqual(encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(encrypt("Python 3.8", 4), "Tcxlsr 3.8")

    def test_decrypt_with_non_alpha(self):
        self.assertEqual(decrypt("bcd123", 1), "abc123")
        self.assertEqual(decrypt("Mjqqt, Btwqi!", 5), "Hello, World!")
        self.assertEqual(decrypt("Tcxlsr 3.8", 4), "Python 3.8")

    def test_encrypt_decrypt(self):
        text = "The quick brown fox jumps over the lazy dog!"
        shift = 10
        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)
        self.assertEqual(decrypted, text)


if __name__ == "__main__":
    unittest.main()
