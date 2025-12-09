class Calculator:
    def __init__(self):
        self.history = []
    def calculate(self, a: float, b: float, op: str) -> float:
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Division by zero")
            result = a / b
        else:
            raise ValueError("Invalid operator")
        entry = f"{a} {op} {b} = {result}"
        self.history.append(entry)
        return result
    def get_history(self):
        return self.history
if __name__ == "__main__":
    calc = Calculator()
    print(calc.calculate(2, 3, '+'))
    print(calc.calculate(10, 5, '/'))
    print("History:")
    for h in calc.get_history():
        print(h)