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
        test_data = Pii()
        self.assertEqual(test_data.has_email(), None)

    def test_has_ipv4(self):
        # Test a valid IPv4 address
        test_data = Pii('176.96.81.20')
        self.assertTrue(test_data.has_ipv4())

    def test_has_ipv6(self):
        # Test a valid IPv6 address
        test_data = Pii('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        self.assertTrue(test_data.has_ipv6())

    def test_has_name(self):
        test_data = Pii()
        self.assertEqual(test_data.has_name(), None)

    def test_has_street_address(self):
        test_data = Pii()
        self.assertEqual(test_data.has_street_address(), None)

    def test_has_credit_card(self):
        #Test case for valid credit card
        test_data = Pii('My card is 1234-1234-1234-1234')
        self.assertTrue(test_data.has_credit_card())
        # Test case for an invalid card
        test_data = Pii('My card is 123456-123456-1234-1234')
        self.assertFalse(test_data.has_credit_card())
        test_data = Pii('My card is 123a-1256-14-124')
        self.assertFalse(test_data.has_credit_card())

    def test_has_at_handle(self):
        #Test case for valid @ handle
        test_data = Pii('My social media handle is @sushi_fein')
        self.assertTrue(test_data.has_at_handle())
        

        #Test case for invalid  @ handle
        test_data = Pii('My social media handle is @.sushifein')
        self.assertFalse(test_data.has_at_handle())
        


    def test_has_pii(self):
        test_data = Pii()
        self.assertEqual(test_data.has_pii(),False)


if __name__ == '__main__':
    unittest.main()
