from json import loads


def getDegree(graphe):
    degree = {}
    sorted_degree = {}
    for k in getSommet(graphe):
        if k in graphe.keys():
            degree[k] = len(graphe[k])
        else:
            degree[k] = 0
    for key in sorted(degree, key=lambda x: -degree[x]):
        sorted_degree[key] = degree[key]
    return sorted_degree


def getSommet(graphe):
    sommet = []
    for i in graphe:
        if i not in sommet:
            sommet.append(i)
    return sommet


def FullGraph(graphe):
    fg = {}
    for sommet in graphe:
        fg[sommet] = graphe[sommet]
        for succ in graphe[sommet]:
            if succ not in fg:
                if succ not in graphe:
                    fg[succ] = []
                else:
                    fg[succ] = graphe[succ]
    return fg


def ordre_pgsg_complet(graphe):
    graphes_complets = []
    for sommet in getDegree(graphe):
        sommets = [sommet]
        updated = True
        for pt in graphe:
            if sommet in graphe[pt]: sommets.append(pt)
        while len(sommets) > 2 and updated:
            for s in sommets:
                updated = False
                for j in sommets[:sommets.index(s)] + sommets[sommets.index(s) + 1:]:
                    if s not in graphe[j]:
                        sommets.remove(s)
                        updated = True
                        break
        graphes_complets.append(sommets)
    pgsg = max(graphes_complets, key=lambda x: len(x))
    return len(pgsg) if len(pgsg) > 2 else False


def Coloration(graphe):
    deg = getDegree(graphe)
    s = getSommet(graphe)
    Colors = {}
    current_color = 1
    color = "Couleur "
    for sommetDeg in deg:
        if sommetDeg not in Colors:
            Colors[sommetDeg] = color + str(current_color)
        for sommet2 in s:
            if sommetDeg in graphe and sommet2 not in graphe[sommetDeg] and sommet2 not in Colors:
                Colors[sommet2] = color + str(current_color)
        if color + str(current_color) in Colors.values():
            current_color += 1
    return Colors


def nombre_chromatique(graphe):
    col = len(set(Coloration(graphe).values()))
    max_len_graphe_complet = ordre_pgsg_complet(FullGraph(graphe))
    if col == max_len_graphe_complet or max_len_graphe_complet == False:
        return "Le nombre chromatique est : " + str(col)
    else:
        return "La coloration realiser n'est pas optimale"


#  {"a": ["c"], "b": ["c","d"], "c": ["a", "b", "d"], "d": ["c", "b", "e"], "e": ["d"]}

#  {"A": ["B", "C", "D", "G"], "B": ["A", "C", "D", "F", "G"], "C": ["A", "B", "D", "F", "G"],"D": ["A", "B", "C", "E", "F"], "E": ["B", "D", "F", "G"], "F": ["C", "D", "E", "G"], "G": ["A", "B", "C", "E", "F"]}
x = input('Entrer un graphe ici : ')
G = loads(x.replace("'", '"'))
print('Coloration trouvée:', Coloration(G))
# print(nombre_chromatique(G))
