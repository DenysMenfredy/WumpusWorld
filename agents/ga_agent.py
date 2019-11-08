

class GaAgent(object):
    def __init__(self, chromosome = None):
        self.fitness=0
        self.chromosome = chromosome if chromosome else self.randomChromosome()
        