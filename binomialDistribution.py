class BinomialDistribution:
    def __init__(self, n, p):
        self.__n = n
        self.__p = p


    @property
    def n(self):
        return self.__n

    @property
    def p(self):
        return self.__p

    def print(self):
        print(f"Your binomial distribution is B({self.n}, {self.p})")

    def fact(self, n):
        if n == 0:
            return 1
        res = 1

        for i in range(2, n + 1):
            res = res * i

        return res
    def get_P(self, k):
        ncr = (self.fact(self.n) / (self.fact(k)
                * self.fact(self.n - k)))
        P = ncr * (self.p ** k) * ((1-self.p)**(self.n - k))
        return P