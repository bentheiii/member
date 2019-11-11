from member import member


class FibonacciSeries:
    def __init__(self, starters=(0, 1)):
        self.n = len(starters)
        for i, v in enumerate(starters):
            self.__call__[i] = v

    @member
    def __call__(self, index):
        return sum(self(index - i) for i in range(1, self.n + 1))


f = FibonacciSeries()
assert f(10) == 55
