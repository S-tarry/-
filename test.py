import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertAlmostEqual(calculator.add(2.5, 3.2), 5.7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(-3, -2), -1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(7, 0), "Error: Division by zero")
        self.assertAlmostEqual(calculator.divide(5.0, 2.0), 2.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculator.add("a", 2)
        with self.assertRaises(TypeError):
            calculator.divide(5, "b")
        with self.assertRaises(TypeError):
            calculator.multiply(None, 4)

if __name__ == "__main__":
    unittest.main()
