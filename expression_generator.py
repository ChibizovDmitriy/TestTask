class ExpressionGenerator:
    def __init__(self, target):
        self.target = target
        self.digits = '9876543210'
        self.results = []

    def backtrack(self, expr, pos, total):
        """
        Рекурсивная функция для генерации всех возможных комбинаций операций между числами.

        Args:
            expr (str): Текущее выражение.
            pos (int): Текущая позиция в строке цифр.
            total (int): Текущее суммарное значение выражения.

        Returns:
            None
        """
        if pos == len(self.digits):
            if total == self.target:
                self.results.append(expr)
            return

        num_str = ''
        for i in range(pos, len(self.digits)):
            num_str += self.digits[i]
            if num_str[0] == '0' and len(num_str) > 1:  # Пропускаем числа с ведущими нулями, кроме 0
                continue
            self.backtrack(expr + '+' + num_str, i + 1, total + int(num_str))
            self.backtrack(expr + '-' + num_str, i + 1, total - int(num_str))

    def generate_expressions(self):
        """Генерирует все возможные выражения."""
        self.backtrack('', 0, 0)

    def print_results(self):
        """Выводит сгенерированные выражения."""
        for result in self.results:
            print(result)
