import numpy as np
import math
import sys
import time
import copy

class SAnnealing(object):

    def __init__(self, domain, step = 1, final_temperature=0.1, temperature = 100, alpha=0.95, equilibrium=10, time = 0):
        self.domain = domain
        self.step = step
        self.temperature = temperature
        self.final_temperature = final_temperature
        self.alpha = alpha
        self.equilibrium = equilibrium
        self.time = time

    def cost_function(self, f, x, COSTOS, REGLAS_PRESEDENCIA):
        return f(x, COSTOS, REGLAS_PRESEDENCIA)


    def create_first_solution(self, f):
        return f(100)


    def create_neighbor_solution(self, f, actual):
        return f(actual)


    def aceptance_probability(self, deltaE, temperature):
        try:
            r = math.exp(deltaE/temperature)
        except OverflowError:
            r = float("inf") 
        return r


    def update_temperature(self, temperature):
        return self.alpha * temperature


    def fit(self, objetive, first, neighbor, COSTOS, REGLAS_PRESEDENCIA, SOLUCION):
        self.cost_ = []
        actual_solution = self.create_first_solution(first)
        best_solution = copy.deepcopy(actual_solution)
        epoch = 0
        number_tested_solution = 0
        aceptanced = 100

        while (self.temperature > self.final_temperature):
            
            number_worst_solution_acepted = 0
            i = 0

            while (i < self.equilibrium): 
                random_solution = self.create_neighbor_solution(f = neighbor, actual = actual_solution) 
                number_tested_solution += 1
                delta_E = self.cost_function(objetive, random_solution, COSTOS, REGLAS_PRESEDENCIA) - self.cost_function(objetive, actual_solution, COSTOS, REGLAS_PRESEDENCIA)
                if delta_E < 0:
                    actual_solution = random_solution.copy()
                else:
                    deg_deltaE = self.aceptance_probability(-delta_E, self.temperature)
                    if(np.random.uniform(0, 1) < deg_deltaE):
                        actual_solution = random_solution.copy()
                        number_worst_solution_acepted += 1
                x = self.cost_function(objetive, actual_solution, COSTOS, REGLAS_PRESEDENCIA)
                self.cost_.append((epoch, x))
                epoch_strlen = len(str(epoch))
                time.sleep(self.time)
                sys.stderr.flush()
                i += 1
                epoch += 1
            aceptanced = number_worst_solution_acepted * 100 /number_tested_solution
            self.temperature = self.update_temperature(self.temperature)

        return(actual_solution)    
        