from random import random

class WeightOptimize:
    size = 3
    fitness_function=None
    
    def __init__(self, generation, count, chromosome = None):
        self.chromosome = chromosome if chromosome else self.randomChromosome()
        self.id = f'{generation}.{count}'
        self.fitness = None
        
    def randomChromosome(self,):
        max_value = 600
        chrom = [ random() * max_value for _ in range(self.size)  ]
        return chrom
    
    def reset(self,):
        pass
        
    def getWeights(self,):
        return (self.chromosome[0], self.chromosome[1], self.chromosome[2])
    
    def __repr__(self,):
        return f'\nChromosome: {self.chromosome}\nFitness: {self.fitness}'
    
    __str__ = __repr__