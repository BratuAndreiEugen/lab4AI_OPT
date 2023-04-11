from algorithm.antcolony import AntColonyOptimization
from utils.reader import Reader


def solver(dinamic):

    #reader = Reader("C:\Proiecte SSD\Python\AntsAI\data\\fricker26.txt")
    reader = Reader("C:\Proiecte SSD\Python\AntsAI\data\\berlin52.txt")
    #m = reader.readMatrix()
    m =  reader.readBerlin()
    n = len(m)
    ants = 24

    alg = AntColonyOptimization(m, n, ants)
    alg.setUp()

    min = 1000000
    g = 0  # nr de generatii
    while g < 100:
        g = g + 1
        if alg.steps % 10 == 0 or alg.steps % 15 == 0:
            min = 1000000
            print("GRAFUL S-A SCHIMBAT")
        sol = alg.getMinCost(dinamic)
        print(str(g) + " Sol = " + str(sol))
        if sol < min:
           min = sol

    print("Best solution : " + str(min))
    print("Path :" + str(alg.getBestPath()))


#solver(False)
solver(True)