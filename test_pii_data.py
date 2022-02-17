import unittest
from pii_data import read_data
from pii_data import Pii


class DataTestCases(unittest.TestCase):
    def test_read_data(self):
        expected_data = ['Aggie Pride Worldwide',
                         'Aggies Do',
                         'Go Aggies',
                         'Aggie Strong!',
                         'Go Aggies',
                         'And Thats on 1891',
                         "Let's Go Aggies",
                         'Never Ever Underestimate an Aggie',
                         'Every Day The Aggie Way',
                         'Can I get an Aggie Pride',
                         'Aggies Do ^2',
                         'Aggie Pride For The Culture',
                         'We Are Aggies! We Are Proud!',
                         'Set My Future Self Up for Success!',
                         'AGGIE PRIDE!',
                         'We are Aggies',
                         'A-G-G-I-E, WHAT? P-R-I-D-E',
                         'Aggie Pride',
                         'Leaders Can Aggies Do',
                         'Mens et Manus',
                         'Aggies Aggies Aggies',
                         'Aggie Pride',
                         'Aggies are always number 1!',
                         'Because thats what Aggies do',
                         'Aggie Bred']

        data = read_data('sample_data.txt')

        self.assertEqual(data, expected_data)

    def test_has_us_phone(self):
        # Test a valid US phone number
        test_data = Pii('My phone number is 970-555-1212')
        self.assertTrue(test_data.has_us_phone())

        # Test a partial US phone number
        test_data = Pii('My number is 555-1212')
        self.assertFalse(test_data.has_us_phone())

        # Test a phone number with incorrect delimiters
        # TODO discuss changing requirements to support this
        test_data = Pii('My phone number is 970.555.1212')
        self.assertFalse(test_data.has_us_phone())

    def test_has_email(self):
        test_data = Pii('My email is user@domain.com')
        self.assertTrue(test_data.has_email())
        test_data = Pii('My email is user@aggies.ncat.com')
        self.assertTrue(test_data.has_email())
        test_data = Pii('My email is user123@domain.com')
        self.assertTrue(test_data.has_email())

        test_data = Pii('My email is user123@')
        self.assertFalse(test_data.has_email())

    def test_has_ipv4(self):
        test_data = Pii('My ip address is 192.0.2.146')
        self.assertTrue(test_data.has_ipv4())
        test_data = Pii('My ip address is 1.7.33.132')
        self.assertTrue(test_data.has_ipv4())

        # bad symbol
        test_data = Pii('My ip address is 1,7,33,132')
        self.assertFalse(test_data.has_ipv4())
        # bad length
        test_data = Pii('My ip address is 1.7.33.132.0')
        self.assertFalse(test_data.has_ipv4())
        # Cant have a number above 256
        test_data = Pii('My ip address is 1.7.33.256.0')
        self.assertFalse(test_data.has_ipv4())
        # Cant have a number below 0
        test_data = Pii('My ip address is 1.7.33.-1.0')
        self.assertFalse(test_data.has_ipv4())

    def test_has_ipv6(self):
        test_data = Pii(
            'My ip address is 2001:1db8:3333:4444:5555:6666:7777:8888')
        self.assertTrue(test_data.has_ipv6())
        test_data = Pii(
            'My ip address is FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF')
        self.assertTrue(test_data.has_ipv6())

        # BAD LENGTH
        test_data = Pii('My ip address is FFFF:FFFF:FFFF:FFFF:FFFF:FFFF')
        self.assertFalse(test_data.has_ipv6())
        # BAD SYMBOL
        test_data = Pii(
            'My ip address is 2001;1db8;3333;4444;5555;6666;7777;8888')
        self.assertFalse(test_data.has_ipv6())
        # Must be hexidecimal (0-9), (a-f), (A-F)
        test_data = Pii(
            'My ip address is 2001:1db8:3333:GGGG:5555:6666:7777:8888')
        self.assertFalse(test_data.has_ipv6())

    def test_has_name(self):
        test_data = Pii('My name is John Smith')
        self.assertTrue(test_data.has_name())
        test_data = Pii('My name is Feng Tang')
        self.assertTrue(test_data.has_name())
        test_data = Pii('My name is Ty Rone')
        self.assertTrue(test_data.has_name())

        # First capital
        test_data = Pii('My name is john Smith')
        self.assertFalse(test_data.has_name())
        # LAst capital
        test_data = Pii('My name is John smith')
        self.assertFalse(test_data.has_name())
        # Conjoined
        test_data = Pii('My name is JohnSmith')
        self.assertFalse(test_data.has_name())

    def test_has_street_address(self):
        test_data = Pii('93 Garfield Street')
        self.assertTrue(test_data.has_street_address())
        test_data = Pii('636 Riverview Road')
        self.assertTrue(test_data.has_street_address())
        test_data = Pii('9104 Littleton Avenue')
        self.assertTrue(test_data.has_street_address())

        # TODO mabye valid idk
        test_data = Pii('9104 Littleton Ave.')
        self.assertFalse(test_data.has_street_address())
        # Missing street#
        test_data = Pii('Littleton Ave.')
        self.assertFalse(test_data.has_street_address())
        # Lowercase
        test_data = Pii('9104 littleton')
        self.assertFalse(test_data.has_street_address())

    def test_has_credit_card(self):
        test_data = Pii('1929-1228-3455-3454')
        self.assertTrue(test_data.has_credit_card())
        test_data = Pii('2345-4567-5678-6789')
        self.assertTrue(test_data.has_credit_card())
        test_data = Pii('2345-1324-3456-1234')
        self.assertTrue(test_data.has_credit_card())
        test_data = Pii('5678-2349-7654-6435')
        self.assertTrue(test_data.has_credit_card())

        # bad symbol
        test_data = Pii('3456=1234=5678=6789')
        self.assertFalse(test_data.has_credit_card())
        # missing symbol
        test_data = Pii('1234764598764567')
        self.assertFalse(test_data.has_credit_card())

    def test_has_at_handle(self):
        test_data = Pii('@tfeng')
        self.assertEqual(test_data.has_at_handle(), None)
        test_data = Pii('@github')
        self.assertEqual(test_data.has_at_handle(), None)
        test_data = Pii('@twitter123')
        self.assertEqual(test_data.has_at_handle(), None)

        # TODO make bad inputs

    def test_has_pii(self):
        # TODO make a long input
        test_data = Pii()
        self.assertEqual(test_data.has_pii(), None)


if __name__ == '__main__':
    unittest.main()
