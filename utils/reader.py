from utils.weird_reader import readFromTSP


class Reader:
    def __init__(self, filename):
        self.__filename = filename
        self.matrix = []
        self.n = 0

    def readMatrix(self):
        try:
            f = open(self.__filename, "r")
        except IOError:
            print("Nu am gasit")

        nr = f.readline()
        n = int(nr)

        linie = f.readline().strip()
        while linie != "":
            el = linie.split(",")
            l = []
            i = 0
            while i < n:
                l.append(int(el[i]))
                i = i + 1
            self.matrix.append(l)
            linie = f.readline().strip()

        f.close()

        return self.matrix

    def readBerlin(self):
        return readFromTSP(self.__filename)

