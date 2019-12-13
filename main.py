from efficience_calculation import EfficienceCalculation

def main():
    size = 7
    #for perc in range(5,90,5):
    # perc = 50
    # print(f'{perc}%')
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
    #weights = [200*size_factor, 250*size_factor, 50*size_factor, -10*size_factor, -0.9*size_factor, 0.8*size_factor, -20*size_factor, -10*size_factor]
    efficience_calulation = EfficienceCalculation("teste-environment")
    efficience_calulation.loadEnvironment(size, size-1)
    efficience_calulation.loadWeights(4*(size**2) ,weights)
    efficience_calulation.runIterations(1, 5)
    efficience_calulation.exportResults()
    efficience_calulation.showResults()
    efficience_calulation.showGraphics()
if __name__ == '__main__':
    main()
