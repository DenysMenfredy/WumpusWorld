
from efficience_calculation import EfficienceCalculation

def main():
    sizes = [10]
    size_chrom = 100
    weights = [
        1000,  # got_gold
        500,  # wumpus_died
        70,  # escaped
        -10,  # agent_died
        -0.5,  # size
        2,    # hits
        -2,   # errors
        -2,   # distance 
        -2,   # fadigue
    ]
    for size in sizes:
        efficience_calulation = EfficienceCalculation("test")
        efficience_calulation.loadEnvironment(size, size-1)
        efficience_calulation.loadWeights(size_chrom ,weights)
        efficience_calulation.runIterations(50, environments = 10)
        # efficience_calulation.exportResults()
    # efficience_calulation = EfficienceCalculation("madrugada")
    # efficience_calulation.showGraphics()
if __name__ == '__main__':
    main()