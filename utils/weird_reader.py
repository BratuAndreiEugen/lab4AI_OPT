import math


def readFromTSP(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
        coords = []
        for line in lines:
            if line.startswith('EOF'):
                break
            if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                parts = line.split()
                x = float(parts[1])
                y = float(parts[2])
                coords.append((x, y))

    # Calcularea distanțelor dintre noduri
    n = len(coords)
    dist_matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((coords[i][0] - coords[j][0]) ** 2 +
                             (coords[i][1] - coords[j][1]) ** 2)
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    graph = {'noNodes': len(dist_matrix),
             'matrix': dist_matrix,
             'noEdges': len(dist_matrix),
             'start': 1,
             'end': 52}
    return graph['matrix']