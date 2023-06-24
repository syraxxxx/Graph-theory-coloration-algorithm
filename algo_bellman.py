from json import loads


def bellMan(graphe, origin_dest):
    chemin_generale = []
    chemin_generale = [[[origin_dest[0]], 0]]
    for chemin in chemin_generale:
        adjascent = getAdjascent(chemin, graphe)
        for ind_adjascent in adjascent:
            var = list(chemin[0])
            var.append(ind_adjascent[0][-1])
            total = chemin[1] + ind_adjascent[1]
            new_chemin = [var, total]
            chemin_generale.append(new_chemin)
    return chemin_generale


def getAdjascent(chemin, graphe):
    val = chemin[0][-1]
    tab = []
    for sommet in graphe:
        if val == sommet:
            for valeur in graphe[val]:
                if valeur[0] not in chemin[0]:
                    chem = [[sommet, valeur[0]], valeur[1]]
                    tab.append(chem)
    return tab


# x = {"A": [["C",5],["B",10]], "B": [["D",6]], "C": [["B",2]],"D":[["C",9]] }
# x = str(x)
x = input('Entrer un graphe ici : ')
G = loads(x.replace("'", '"'))
# G = {'A': [['C', 5], ['B', 10]], 'B': [['D', 6]], 'C': [['B', 2], ['D', 9]]}
origin_dest = ["A", "D"]
bellMan(G, origin_dest)
