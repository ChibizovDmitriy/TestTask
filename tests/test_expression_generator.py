import unittest
from expression_generator import ExpressionGenerator


class TestExpressionGenerator(unittest.TestCase):
    def test_generate_expressions(self):
        expression_generator = ExpressionGenerator(200)
        expression_generator.generate_expressions()

        # Проверяем, что результаты не пусты
        self.assertTrue(expression_generator.results)

        # Проверяем, что все результаты корректны
        for result in expression_generator.results:
            self.assertEqual(eval(result), 200)

    def test_generate_expressions_target_0(self):
        expression_generator = ExpressionGenerator(0)
        expression_generator.generate_expressions()

        # Проверяем, что результаты не пусты
        self.assertTrue(expression_generator.results)

        # Проверяем, что все результаты корректны
        for result in expression_generator.results:
            self.assertEqual(eval(result), 0)

    def test_generate_expressions_target_negative(self):
        expression_generator = ExpressionGenerator(-200)
        expression_generator.generate_expressions()

        # Проверяем, что результаты не пусты
        self.assertTrue(expression_generator.results)

        # Проверяем, что все результаты корректны
        for result in expression_generator.results:
            self.assertEqual(eval(result), -200)

    def test_generate_expressions_target_large(self):
        expression_generator = ExpressionGenerator(99999)
        expression_generator.generate_expressions()

        # Проверяем, что результаты пусты - значение 99999 не является достижимым
        self.assertTrue(len(expression_generator.results) == 0)


if __name__ == '__main__':
    unittest.main()
