from expression_generator import ExpressionGenerator

if __name__ == "__main__":
    # Создаем экземпляр класса ExpressionGenerator с целевым числом 200
    expression_generator = ExpressionGenerator(200)

    # Генерируем выражения
    expression_generator.generate_expressions()

    # Выводим результаты
    expression_generator.print_results()
