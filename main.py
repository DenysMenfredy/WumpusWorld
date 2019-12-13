from efficience_calculation import EfficienceCalculation

def main():
    size = 4
    weights = [
        200,  # got_gold
        250,  # wumpus_died
        70,  # escaped
        -5,  # agent_died
        -0.5, # size
        0.1,    # hits
        -1,   # errors
        -5    # distance
    ]
    efficience_calulation = EfficienceCalculation("teste-environment")
    efficience_calulation.loadEnvironment(size, size-1)
    efficience_calulation.loadWeights(4*(size**2) ,weights)
    efficience_calulation.runIterations(1, 1)
    #efficience_calulation.exportResults()
    efficience_calulation.showResults()
    #efficience_calulation.showGraphics()

if __name__ == '__main__':
    main()
