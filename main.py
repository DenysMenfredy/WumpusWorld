from efficience_calculation import EfficienceCalculation

def main():
    size = 5
    #for perc in range(5,90,5):
    perc = 50
    size_factor = size * perc/100
    print(f'{perc}%')
    #weights = [300, 350, 100, -10, -0.9, 0.8, -3, -10]
    weights = [200*size_factor, 250*size_factor, 50*size_factor, -10*size_factor, -0.9*size_factor, 0.8*size_factor, -20*size_factor, -10*size_factor]
    efficience_calulation = EfficienceCalculation("teste-environment")
    efficience_calulation.loadEnvironment(size, size-1)
    efficience_calulation.loadWeights(200*size_factor ,weights)
    efficience_calulation.runIteration(1)
    #efficience_calulation.exportResults()
    efficience_calulation.showResults()
    #efficience_calulation.showGraphics("teste-iterations")
if __name__ == '__main__':
    main()
