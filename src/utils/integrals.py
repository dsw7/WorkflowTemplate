class SimpleIntegral:
    """
    Get the first 5 integrals of the simple function:
        f(x) = x
    """

    def __init__(self, x):
        self.x = x

    def get_first_integral(self):
        return (1 / 2) * self.x ** 2

    def get_second_integral(self):
        return (1 / 6) * self.x ** 3

    def get_third_integral(self):
        return (1 / 24) * self.x ** 4

    def get_fourth_integral(self):
        return (1 / 120) * self.x ** 5

    def get_fifth_integral(self):
        return (1 / 720) * self.x ** 6
