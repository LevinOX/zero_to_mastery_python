import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''Test 1'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        """Test 2"""
        test_param = 'fsdaijfo'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        """Test 3"""
        test_param = (1, 2)
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        """Test 4"""
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        """Test 5"""
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff6(self):
        """Test 6"""
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
