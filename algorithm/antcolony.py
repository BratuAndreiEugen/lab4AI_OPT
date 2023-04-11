from random import randint


class AntColonyOptimization:

    def __init__(self, matrix, n, m):
        # adjacency matrix
        self.matrix = matrix

        # number of nodes
        self.n = n

        # number of ants
        self.m = m

        # ant list
        self.ants = []

        # matrix with pheromone quantity
        self.pheromone = []

        # matrix with pheromone intensity
        self.pheromoneIntensity = []

        # for each ant we map a list of visited cities : 0 if not visited, 1 if visited
        self.visited = []

        # for each ant we save the path it takes at a certain given moment
        self.paths = []

        # for each ant we also save the cost of the path it took
        self.costs = []

        self.steps = 0
        self.bestPath = []

    def setUp(self):
        for i in range(0, self.m):
            self.ants.append(i)
            self.paths.append([])
            self.costs.append(0)
            self.visited.append([])
            for j in range(0, self.m):
                self.visited[i].append(0)

        # pheromone matrix
        for i in range(0, self.n):
            pher = []
            intensity = []
            for j in range(0, self.n):
                v = randint(0, 1)
                intensity.append(v)
                pher.append(0)

            self.pheromoneIntensity.append(intensity)
            self.pheromone.append(pher)



    def modifyWeights(self):
        added_weight = randint(0, 1)
        for i in range(0, self.n):
            for j in range(0, self.n):
                v = randint(0, 1)
                if self.matrix[i][j] > 0 and v == 1:
                    self.matrix[i][j] = self.matrix[i][j] + added_weight

    def cutPath(self):
        l = randint(0, self.n-1)
        c = randint(0, self.n-1)
        while self.matrix[l][c] == 0:
            l = randint(0, self.n - 1)
            c = randint(0, self.n - 1)
        self.matrix[l][c] = 1000000

    def addPath(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.matrix[i][j] == 1000000 and i != j:
                    self.matrix[i][j] = randint(1, 100)
                    break

    def getBestPath(self):
        return self.bestPath

    def checkValidity(self, visited_vector):
        for i in visited_vector:
            if i == 0:
                return True
        return False

    def chooseNextNode(self, node, ant):
        cost = 0
        for i in range(len(self.matrix[node])):
            cost += self.matrix[node][i]
        min = 10000000
        chosenNode = -1
        for i in range(0, self.n):
            # formula (pheromone on path+weight of the path)/totalCost
            f = 0
            if cost != 0:
                f = (self.pheromone[node][i] + self.matrix[node][i])/cost
            else:
                print("HOW is cost 0 ? / chooseNextNode")

            if self.matrix[node][i] > 0 and f < min and self.visited[ant][i] == 0:
                min = f
                chosenNode = i

        return chosenNode

    def solve(self):

        findable = 1
        for ant in self.ants:
            # each ant starts on it's own node
            cost = 0
            source = ant
            self.visited[ant][source] = 1
            self.paths[ant].append(source)

            # the position of the last visited node in the path
            lastVisited = len(self.paths[ant]) - 1
            while self.checkValidity(self.visited[ant]) != 0 and findable == 1:
                nextNode = self.chooseNextNode(self.paths[ant][lastVisited], ant)
                if nextNode != -1:
                    self.visited[ant][nextNode] = 1
                    lastVisited += 1
                    self.paths[ant].append(nextNode)
                    cost += self.matrix[self.paths[ant][lastVisited-1]][self.paths[ant][lastVisited]]
                    a = randint(0,1)
                    self.pheromone[ant][nextNode] = (1-a)*self.pheromone[ant][nextNode] + a*self.pheromoneIntensity[ant][nextNode]

                else:
                    findable = 0

            cost += self.matrix[source][lastVisited]

            self.costs[ant] = cost


    # this is the main body of the algorithm
    def getMinCost(self, dinamic):
        minim = 10000000


        self.steps = self.steps + 1
        self.visited = []

        if dinamic == True:
            if self.steps % 10 == 0:
                self.modifyWeights()
            if self.steps % 15 == 0:
                self.cutPath()
            if self.steps % 20 == 0:
                self.addPath()

        for i in range(0, self.m):
            l = []
            for j in range(0, self.n):
                l.append(0)
            self.visited.append(l)

        self.paths = []
        self.costs = []
        for i in range(0, self.m):
            self.paths.append([])
            self.costs.append(0)

        self.solve()

        for cost in self.costs:
            if cost < minim and cost != 0:
                minim = cost

        for ant in self.ants:
            if self.costs[ant] == minim:
                self.bestPath = self.paths[ant]


        return minim



