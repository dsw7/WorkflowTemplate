class SimpleDerivative:
    """
    Get the first five derivates of the function:
        f(x) = x ** 6 / 720
    """

    def __init__(self, x):
        self.x = x

    def get_fifth_derivative(self):
        return self.x

    def get_fourth_derivative(self):
        return (1 / 2) * self.x ** 2

    def get_third_derivative(self):
        return (1 / 6) * self.x ** 3

    def get_second_derivative(self):
        return (1 / 24) * self.x ** 4

    def get_first_derivative(self):
        return (1 / 120) * self.x ** 5
