import unittest
from Tests_Coverage.app import factorial
from app import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30), 1346269)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1),1)

#if __name__ == "__main__":
#   unittest.main()

#pytest .\Tests_Coverage\test_app.py

#pip install coverage 

#coverage run .\Tests_Coverage\app.py

#coverage report .\Tests_Coverage\app.py

#pip install pytest-cov

#pytest --cov=test_app.py