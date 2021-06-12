from django.test import TestCase
import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        """
        Method called to prepare the test fixture.
        This is called immediately before calling the test method
        :return:
        """
        print("Setup Method Called")

    def tearDown(self):
        """
        Method called immediately after the test method has been called and the result recorded.
        :return:
        """
        print("Tear Down Method Called")

    def test_upper(self):
        print("Func to check upper case")
        self.assertEqual('foo'.upper(), 'FOO')

        # Returns TRUE if the string is in uppercase

    # else returns False.
    @unittest.expectedFailure
    def test_isupper(self):
        self.assertTrue('FOo'.isupper())
        self.assertFalse('foo'.isupper())

        # Returns true if the string is stripped and

    # matches the given output.
    def test_strip(self):
        s = 'Hello world'
        self.assertEqual(s.strip('Hello'), ' world')

        # Returns true if the string splits and matches

    # the given output.
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.skip("Issue with current build, so skipping this func")
    def test_sample_2(self):
        x = 12
        y = 11
        print("Comparing x and y values")
        self.assertEqual(x, y, msg="x and y values are same")


if _name_ == "_main_":
    unittest.main()

# Create your tests here.
