from efficience_calculation import EfficienceCalculation

def main():
    weights = [300, 350, 500, -10, -0.7, 0.333, -2, -10]
    efficience_calulation = EfficienceCalculation("teste-environment")
    efficience_calulation.loadEnvironment(5, 4)
    efficience_calulation.loadWeights(weights)
    efficience_calulation.runIteration(1)
    #efficience_calulation.exportResults()
    efficience_calulation.showResults()
    #efficience_calulation.showGraphics("teste-iterations")
if __name__ == '__main__':
    main()
