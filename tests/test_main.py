import unittest
from main import simple_count, complex_function


class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(0, simple_count('hello'))

    # def test_complex_function(self):
    #     self.assertEqual('behaviour 1', complex_function())

    # collected new test case from ChatGPT for looping idea
    def test_complex_function_loop(self):
        for _ in range(1000):
            result = complex_function()
            if result == 'behaviour 1':
                # If any output matches, consider the test passed
                return
        # If none of the outputs match, the test fails
        self.fail("No output matched 'behaviour 1' after 1000 attempts")
