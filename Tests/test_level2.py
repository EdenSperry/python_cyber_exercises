import unittest
from level2 import check_password_strength  # Assuming your code is in a file named password_strength_module.py

class TestCheckPasswordStrength(unittest.TestCase):

    def test_strong_passwords(self):
        self.assertEqual(check_password_strength("Strong1!"), "Strong password.")
        self.assertEqual(check_password_strength("Passw0rd$"), "Strong password.")
        self.assertEqual(check_password_strength("C0mpl3x#Pwd"), "Strong password.")
        self.assertEqual(check_password_strength("Aa1@aa1@"), "Strong password.")

    def test_weak_passwords(self):
        self.assertEqual(check_password_strength("short"), "Password too short. It must be at least 8 characters long.")
        self.assertEqual(check_password_strength("alllowercase"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")
        self.assertEqual(check_password_strength("ALLUPPERCASE"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")
        self.assertEqual(check_password_strength("12345678"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")
        self.assertEqual(check_password_strength("NoSpecialChar1"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")
        self.assertEqual(check_password_strength("NoDigits!"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")
        self.assertEqual(check_password_strength("NOLOWERCASE1!"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")
        self.assertEqual(check_password_strength("nouppercase1!"), "Weak password. Ensure it has uppercase, lowercase, digits, and special characters.")

if __name__ == "__main__":
    unittest.main()
