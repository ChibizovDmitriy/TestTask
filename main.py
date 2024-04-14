from expression_generator import ExpressionGenerator

if __name__ == "__main__":
    # Создаем экземпляр класса ExpressionGenerator с целевым числом 200
    # M=200
    # в коде модуля M=target
    N = 0
    M = 0
    input(M)
    input
    expression_generator = ExpressionGenerator(M)

    # Генерируем выражения
    expression_generator.generate_expressions()

    # Выводим результаты
    expression_generator.print_results()
