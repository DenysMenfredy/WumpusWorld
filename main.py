from math import ceil

from efficience_calculation import EfficienceCalculation

def main():
    size = 25
    n_pits = ceil((size*size - 2) * 0.10)
    # weights = [
    #     200,  # got_gold
    #     250,  # wumpus_died
    #     70,  # escaped
    #     -5,  # agent_died
    #     -0.5, # size
    #     2,    # hits
    #     -1,   # errors
    #     -5    # distance
    # ]
    weights = [
        1000,  # got_gold
        500,  # wumpus_died
        70,  # escaped
        -10,  # agent_died
        -0.25,  # size
        1,    # hits
        -1,   # errors
        -1,    # distance 
        -1,   # fadigue
    ]
    efficience_calulation = EfficienceCalculation("teste-environment")
    efficience_calulation.loadEnvironment(size, n_pits)
    # size_chrom = int(104.7*size -473.7)
    size_chrom = 100
    # print(size_chrom)
    # quit()
    efficience_calulation.loadWeights(size_chrom ,weights)
    efficience_calulation.clearData()
    efficience_calulation.runIterations(1, environments = 5)
    #efficience_calulation.exportResults()
    efficience_calulation.showResults()
    #efficience_calulation.showGraphics()

if __name__ == '__main__':
    main()
