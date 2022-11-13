import numpy as np
import matplotlib.pyplot as plt
import Config


class Population:
    def __init__(self, alpha: float, N: int, id: int):
        self.array_N = []
        self.alpha = alpha
        self.N = N
        self.id = id

    def multiplication(self):
        return self.alpha * self.N

    def __str__(self):
        return f"id: {self.id} alpha: {self.alpha}  N: {self.N}"

    def interaction(self, populations):
        self.array_N.append(self.N)
        f = 0
        for population in populations:
            if self == population:
                continue
            f += Config.coefficients[self.id][population.id] * population.N * self.N
        self.N += Config.delta * (self.multiplication() + f)
        print("----------------")