import matplotlib.pyplot as plt

#a - vertical b - horizontal
def intersect(a, b):
    if(((a[1] < b[0] and a[2] > b[0]) or (a[1] > b[0] and a[2] < b[0])) and 
    ((b[1] < a[0] and b[2] > a[0]) or (b[1] > a[0] and b[2] < a[0]))):
        return True
    else:
        return False

def filt_hor(vert):
    ar = []
    for i in range(len(vert)):
        if(vert[i][1] == vert[(i + 1) % len(vert)][1]):
            ar.append([vert[i][1], vert[i][0], vert[(i + 1) % len(vert)][0]])
    return ar

def filt_vert(vert):
    ar = []
    for i in range(len(vert)):
        if(vert[i][0] == vert[(i + 1) % len(vert)][0]):
            ar.append([vert[i][0], vert[i][1], vert[(i + 1) % len(vert)][1]])
    return ar

def check(a, b):
    a.sort(key = lambda x: x[0])
    b.sort(key = lambda x: x[0])
    test_edge = [(a[0][1] + a[0][2]) / 2 + 0.25, b[0][0] - 0.5, b[-1][0] + 0.5]
    vector = []
    for i in a:
        if(intersect(i, test_edge)):
            vector.append([i[0], 1])
    for i in b:
        if(intersect(i, test_edge)):
            vector.append([i[0], 0])
    vector.sort(key = lambda x: x[0])
    a_index = 0
    b_index = 0
    for i in vector:
        if(b_index):
            if(i[1]):
                return 1
        if(a_index):
            if(i[1] == 0):
                return -1
        if(i[1] == 0):
            b_index = (b_index + 1) % 2
        else:
            a_index = (a_index + 1) % 2

    test_edge = [(b[0][1] + b[0][2]) / 2 + 0.25, a[0][0] - 0.5, a[-1][0] + 0.5]
    vector = []
    for i in b:
        if(intersect(i, test_edge)):
            vector.append([i[0], 1])
    for i in a:
        if(intersect(i, test_edge)):
            vector.append([i[0], 0])
    vector.sort(key = lambda x: x[0])
    a_index = 0
    b_index = 0
    for i in vector:
        if(a_index):
            if(i[1]):
                return -1 # ТУТ ПОДУМАТЬ
        if(b_index):
            if(i[1] == 0):
                return 1
        if(i[1] == 0):
            a_index = (a_index + 1) % 2
        else:
            b_index = (b_index + 1) % 2
    return 0

def rescale(cycles):
    vertical_levels = []
    horizontal_levels = []
    for i in cycles:
        for j in range(len(i)):
            if(j % 2):
                if(not (i[j][0] in vertical_levels)):
                    vertical_levels.append(i[j][0])
            else:
                if(not (i[j][0] in horizontal_levels)):
                    horizontal_levels.append(i[j][0])
    horizontal_levels.sort()
    vertical_levels.sort()
    for i in cycles:
        for j in range(len(i)):
            if(j % 2):
                i[j][0] = vertical_levels.index(i[j][0])
                i[j][1] = horizontal_levels.index(i[j][1])
                i[j][2] = horizontal_levels.index(i[j][2])
            else:
                i[j][0] = horizontal_levels.index(i[j][0])
                i[j][1] = vertical_levels.index(i[j][1])
                i[j][2] = vertical_levels.index(i[j][2])

def lie_in(edge, current_edge):
    current_edge.sort(key = lambda x: min(x[1], x[2]))
    if edge[1] > 0:
        for i in current_edge:
            if min(edge[0][1], edge[0][2]) > min(i[1], i[2]) and max(edge[0][1], edge[0][2]) < max(i[1], i[2]):
                return [2, i]
        return [0,[]]
    else:
        # print(current_edge, edge, "KEKW")
        for i in range(len(current_edge)):

            if min(edge[0][1], edge[0][2]) == max(current_edge[i][1], current_edge[i][2]) and max(edge[0][1], edge[0][2]) ==  min(current_edge[i + 1][1], current_edge[i + 1][2]):
                return [3, current_edge[i], current_edge[i + 1]]
            if min(edge[0][1], edge[0][2]) == min(current_edge[i][1], current_edge[i][2]) and max(edge[0][1], edge[0][2]) == max(current_edge[i][1], current_edge[i][2]):
                return [1, current_edge[i]]
    return [0]

def number_of_vertical_lines(cycles):
    max_ = 0
    for i in cycles:
        for j in range(len(i)):
            if(j % 2):
                max_ = max(i[j][0], max_)
    return max_



def rescale_2(vert_e, hor_e):
    vertical_levels = []
    horizontal_levels = []

    for j in vert_e:
        if(not (j[0] in vertical_levels)):
            vertical_levels.append(j[0])    
    for i in hor_e:
        if(not (i[0] in horizontal_levels)):
            horizontal_levels.append(i[0])
    horizontal_levels.sort()
    vertical_levels.sort()
    for i in vert_e:
        i[0] = vertical_levels.index(i[0])
        i[1] = horizontal_levels.index(i[1])
        i[2] = horizontal_levels.index(i[2])
    for i in hor_e:
        i[0] = horizontal_levels.index(i[0])
        i[1] = vertical_levels.index(i[1])
        i[2] = vertical_levels.index(i[2])

def check_all(r):
    for i in r:
        for j in i:
            for k in r:
                for l in k:
                    result = 0
                    if l == j:
                        continue
                    if j[1] > j[3]:
                        if l[1] > l[3]:
                            if l[2] < j[0] or l[0] > j[2] or (l[0] < j[0] and l[2] > j[2] and l[1] > j[1] and l[3] < j[3]) or (j[0] < l[0] and j[2] > l[2] and j[1] > l[1] and j[3] < l[3]):
                                result = 1
                        else:
                            if (l[1] > j[3] and l[3] < j[1]) or l[2] < j[0] or l[0] > j[2]:
                                result = 1
                            #share verice or two
                            if (l[3] <= j[1] and l[1] >= j[3]) and (l[2] <= j[0] or l[0] >= j[2]):
                                result = 1
                            #good intersection
                            if (l[1] > j[1] or l[3] < j[3]) and l[0] < j[0] and l[2] > j[2]:
                                result = 1
                    else:
                        if l[1] > l[3]:
                            if (j[1] > l[3] and j[3] < l[1]) or j[2] < l[0] or j[0] > l[2]:
                                result = 1
                            #share verice or two
                            if (j[3] <= l[1] and j[1] >= l[3]) and (j[2] <= l[0] or j[0] >= l[2]):
                                result = 1
                            #good intersection
                            if (j[1] > l[1] or j[3] < l[3]) and j[0] < l[0] and j[2] > l[2]:
                                result = 1
                        else:
                            #dosent intersect
                            if l[2] < j[0] or l[0] > j[2] or j[1] > l[3] or j[3] < l[1]:
                                result = 1
                            #share a vertice
                            if ((l[0] >= j[2] or l[2] <= j[0]) and l[1] >= j[3]) or ((l[0] >= j[2] or l[2] <= j[0]) and l[3] <= j[1]):
                                result = 1
                            #good intersection
                            if j[0] < l[0] and j[2] > l[2] and j[1] > l[1] and j[3] < l[3]:
                                result = 1
                            if l[0] < j[0] and l[2] > j[2] and l[1] > j[1] and l[3] < j[3]:
                                result = 1
                    if result != 1:
                        print('ahahaha')
                        print(l, j)

#функция добавляющая зизаги, чтобы в одной окружности зейферта не было двух вертикальных ребер на одном уровне
def add_more_zigzags(vert_e, hor_e):
    vert_to_delete = []
    vert_to_append = []
    hor_to_append = []
    for i in vert_e:
        to_delete_hor = []
        hor_to_change = []
        for j in hor_e:
            if intersect(i, j):
                to_delete_hor.append(j)
            if (i[0] == j[1] or i[0]== j[2]) and (max(i[1], i[2]) == j[0]):
                hor_to_change =  j 
        to_delete_hor.sort(key = lambda x: x[0])
        if len(to_delete_hor) > 1:
            orient = 0.5 if i[2] > i[1] else -0.5 #отвечает за то, в какую сторону идет кривая
            vert_to_delete.append(i)
            for j in range(len(to_delete_hor)):
                hor_to_append.append([to_delete_hor[j][0] + 0.5 / (i[0] + 1), i[0] - (j + (int)(0.5 - orient)) / (3 * len(to_delete_hor)), i[0] - (j + (int)(0.5 + orient)) / (3 * len(to_delete_hor))])
                if j != 0:
                    vert_to_append.append([i[0] - j / (3 * len(to_delete_hor)), to_delete_hor[j +(int)(-0.5 - orient)][0] + 0.5 / (i[0] + 1), to_delete_hor[j + (int)(-0.5 + orient)][0] + 0.5 / (i[0] + 1)])
            vert_to_append.append([i[0], min(i[1], i[2]), to_delete_hor[0][0] + 0.5 / (i[0] + 1)] if orient > 0 else [i[0], to_delete_hor[0][0] + 0.5 / (i[0] + 1), min(i[1], i[2])])
            vert_to_append.append([i[0] - 1/3, to_delete_hor[-1][0] + 0.5 / (i[0] + 1), max(i[1], i[2])] if orient > 0 else [i[0] - 1/3, max(i[1], i[2]), to_delete_hor[-1][0] + 0.5 / (i[0] + 1)])
            hor_e.append([hor_to_change[0], (i[0] - 1/3) if orient > 0 else hor_to_change[1], hor_to_change[2] if orient > 0 else (i[0] - 1/3)])
            hor_e.remove(hor_to_change)
    hor_e += hor_to_append
    for v in vert_to_delete:
        vert_e.remove(v)
    vert_e += vert_to_append


def number_of_rows(cycles):
    max_ = 0
    for i in cycles:
        for j in range(len(i)):
            if j % 2 == 0:
                max_ = max(i[j][0], max_)
    return max_


def number_of_columns(cycles):
    max_ = 0
    for i in cycles:
        for j in range(len(i)):
            if j % 2:
                max_ = max(i[j][0], max_)
    return max_






if __name__ == "__main__":
    #vert = [[0, 3], [0, 44], [16, 44], [16, 37], [43, 37], [43, 1], [23, 1], [23, 6], [38, 6],[38, 43], [15, 43], [15, 34], [13, 34], [13, 16], [2, 16], [2, 11] ,[9, 11], [9, 29], [5, 29],[5, 25], [17, 25], [17, 0], [44, 0], [44, 27], [11, 27], [11, 15], [21, 15], [21, 17], [12, 17],[12, 12], [3, 12], [3, 4], [18, 4], [18, 41], [42, 41], [42, 2], [4, 2], [4, 10], [8, 10],[8, 28], [14, 28], [14, 35], [34, 35], [34, 26], [6, 26], [6, 5], [37, 5], [37, 9], [26, 9],[26, 20], [7, 20], [7, 24], [33, 24], [33, 39], [29, 39], [29, 33], [31, 33], [31, 23], [10, 23],[10, 19], [41, 19], [41, 42], [27, 42], [27, 14], [24, 14], [24, 31], [19, 31], [19, 7], [22, 7],[22, 30], [32, 30], [32, 40], [40, 40], [40, 22], [25, 22], [25, 13], [20, 13], [20, 32], [30, 32],[30, 38], [39, 38], [39, 8], [35, 8], [35, 36], [28, 36], [28, 21], [1, 21], [1, 18], [36, 18],[36, 3]]
    #vert = [[0, 0], [0, 3], [3, 3], [3, 1], [1, 1], [1, 4], [2, 4], [2, 2], [4, 2], [4, 0]]
    #vert = [[0, 0], [0, 7], [3, 7], [3, 4], [1, 4], [1, 6], [5, 6], [5, 2], [2, 2], [2, 5], [6, 5], [6, 1], [4, 1], [4, 3], [7, 3], [7, 0]]
    #vert = [[0, 4], [2, 4], [2, 2], [4, 2], [4, 0], [1, 0], [1, 3], [3, 3], [3, 1], [0, 1]]
    #vert = [[0,0], [0,1], [1,1], [1, 2], [2, 2], [2, 0]]
    vert = [[0, 0], [0, 2], [3, 2], [3, 5], [1, 5], [1, 7], [7, 7], [7, 4], [5, 4], [5, 6], [6, 6], [6, 1], [2, 1], [2, 3], [4, 3], [4, 0]]
    #vert = [[0, 0], [0, 8], [8, 8], [8, 10], [2, 10], [2, 1], [1, 1], [1, 9], [6, 9], [6, 4], [4, 4], [4, 6], [5, 6], [5, 2], [3, 2], [3, 5], [10, 5], [10, 7], [9, 7], [9, 3], [7, 3], [7, 0]]
    #sorted
    hor_e = sorted(filt_hor(vert), key = lambda x: x[0])
    #Ребра лежат так: [row, begin, end] sorted
    vert_e = sorted(filt_vert(vert), key = lambda x: x[0])
    #Ребра лежат так: [column, begin, end] sorted

    #хотим избежать двух вертикальных ребер на одном уровне в одной окржности зейферта
    add_more_zigzags(vert_e, hor_e)
    
    hor_e.sort(key = lambda x: x[0])
    vert_e.sort(key = lambda x: x[0])

    rescale_2(vert_e, hor_e) #отнормировали сетку
    rows = hor_e[-1][0] + 1 
    cycles = []
    while(len(hor_e) > 0):
        v_start = [hor_e[0][1], hor_e[0][0]] #начальная точка. по ней судим, когда зациклились
        v_current = [hor_e[0][2], hor_e[0][0]] #текущая вершина
        edge_current = hor_e[0] #текущее ребро
        cycle = []
        while (True):
            for i in sorted(vert_e, key = lambda x: x[0], reverse = False if (edge_current[1] < edge_current[2]) else True):
                #надо в правильном порядке проходить
                if(intersect(i, edge_current)):
                    hor_e.remove(edge_current)
                    hor_e.append([edge_current[0], edge_current[1], i[0]])
                    hor_e.append([edge_current[0], i[0], edge_current[2]])
                    
                    vert_e.append([i[0], i[1], edge_current[0]])
                    vert_e.append([i[0], edge_current[0], i[2]])

                    edge_current = [edge_current[0], edge_current[1], i[0]]
                    
                    cycle.append(edge_current)
                    edge_current = [i[0], edge_current[0], i[2]]
                    vert_e.remove(i)
                    break
                if(v_current == [i[0], i[1]]):
                    cycle.append(edge_current)
                    edge_current = i
                    break

            v_current = [edge_current[0], edge_current[2]]
            for i in sorted(hor_e, key = lambda x: x[0], reverse = False if (edge_current[1] < edge_current[2]) else True):
                #тут и выше могут стоять не те неравенства
                if(intersect(edge_current, i)):
                    vert_e.remove(edge_current)
                    vert_e.append([edge_current[0], edge_current[1], i[0]])
                    vert_e.append([edge_current[0], i[0], edge_current[2]])
                    
                    hor_e.append([i[0], i[1], edge_current[0]])
                    hor_e.append([i[0], edge_current[0], i[2]])

                    edge_current = [edge_current[0], edge_current[1], i[0]]
                    
                    cycle.append(edge_current)
                    edge_current = [i[0], edge_current[0], i[2]]
                    hor_e.remove(i)
                    break
                if(v_current == [i[1], i[0]]):
                    cycle.append(edge_current)
                    edge_current = i
                    break
            v_current = [edge_current[2], edge_current[0]]
            if([edge_current[1], edge_current[0]]== v_start):
                break
        j = 0
        for i in cycle:
            if(j % 2):
                vert_e.remove(i)
            else:
                hor_e.remove(i)
            j += 1
        cycles.append(cycle)
    dead_list = []
    for cyc in cycles:
        for j in range(len(cyc)):
            if j % 2 == 0:
                if((cyc[j][2] - cyc[j][1]) * (cyc[(j + 2) % len(cyc)][2] - cyc[(j + 2) % len(cyc)][1]) > 0):
                    dead_list.append([cyc[j + 1].copy(), 1] if((cyc[j][2] - cyc[j][1]) * (cyc[j + 1][2] - cyc[j + 1][1]) < 0) else [cyc[j + 1].copy(), -1])
    m = len(dead_list) #костыль мб потом пригодится. Нужен, если на одной вертикали надо удалить несколько ребер
    dead_list.sort(key = lambda x: x[0][0] + (m - x[0][1]) / m)
    cyrcle_to_delete = []
    for i in dead_list:
        index = 0
        for j in cycles:
            for k in range(len(j)):
                if(j[k] == i[0] and k % 2 == 1):
                    #delete
                    cyrcle_to_delete = j
                    index = k
                    if(i[0][2] > i[0][1]):
                        j[k][2] = j[k][2] - 0.1
                    else:
                        j[k][1] = j[k][1] - 0.1
                    continue
                if(k % 2 == 1):
                    #vertical
                    if(j[k][0] == i[0][0] and j[k][1] > i[0][1]):
                        #грубо говоря, ребро лежит на уровне, который мы хотим подвинуть и выше нашего
                        j[k][0] = i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1)
                else:
                    
                    if(j[k][0] < max(i[0][1], i[0][2])):
                        continue
                    #отсекаем случай, когда ребро лежит выше
                    if(j[k][1] == i[0][0]):
                        j[k][1] = i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1)
                    if(j[k][2] == i[0][0]):
                        j[k][2] = i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1)
                    
                    #horizontal

        #все зависит от того вниз или вверх мы идем
        if(i[0][2] > i[0][1]):
            cyrcle_to_delete.insert(index + 1, [i[0][2] - 0.1, i[0][0], i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1)])
            cyrcle_to_delete.insert(index + 2, [i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1) , i[0][2] - 0.1, i[0][2]])
        else:
            cyrcle_to_delete.insert(index, [i[0][1] - 0.1, i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1), i[0][0]])
            #в строчке ниже может таиться опасность
            cyrcle_to_delete.insert(index, [i[0][0] + i[1] * (i[0][1] + 1) / (2 * rows + 1), i[0][1], i[0][1] - 0.1])
    rescale(cycles)
    n = len(cycles)
    incendent =  [[0] * n for i in range(n)]


    #ОСНОВНОЙ АЛГОРИТМ
    for i in range(n):
        for j in range(n):
            if(i == j):
                incendent[i][j] = 0
                continue
            if(i > j):
                incendent[i][j] = check(cycles[i][1::2], cycles[j][1::2])
                incendent[j][i] = -check(cycles[i][1::2], cycles[j][1::2])
                # 1 - j-ый содержит i-ый
                # -1 - наоборот
                # 0 disjoint'
    level_number = []
    for i in range(n):
        res = 0
        for j in range(n):
            if(incendent[j][i] > 0):
                 res += 1
        level_number.append(res)
    cycles_copy = cycles.copy()
    cycles.sort(reverse = False, key = lambda x: level_number[cycles_copy.index(x)])
    rectangles = []

    vertices = []
    vertical_lines = [] # вертикальные лоскутки, заполненные на предыдущем уровне, которые надо обойти
    # представляют собой набор точек, надо отступить на 1/н
    n = number_of_vertical_lines(cycles)
    for i in range(len(cycles)):
        vertical_line = []
        vertice = []

        rectangle = [] # x1 y1 x2 y2
        cycles_vertical = cycles[i][1::2] # only verical edges needed
        cycles_vertical.sort(key = lambda x: x[0]) #left -> right
        current_edge = []
        for j in  range(len(cycles_vertical)):
            if j < len(cycles_vertical) - 1 and cycles_vertical[j][0] == cycles_vertical[j + 1][0] and cycles[i][cycles[i].index(cycles_vertical[j]) - 1][2] < cycles[i][cycles[i].index(cycles_vertical[j]) - 1][1]:
                cycles_vertical[j], cycles_vertical[j + 1] = cycles_vertical[j + 1], cycles_vertical[j]
        for j in  range(len(cycles_vertical)):
            if current_edge == []:
                result = [0]
            else:
                result = lie_in([cycles_vertical[j], -1 if cycles[i][cycles[i].index(cycles_vertical[j]) - 1][2] > cycles[i][cycles[i].index(cycles_vertical[j]) - 1][1] else 1], current_edge)
            if result[0] == 0:
                current_edge.append(cycles_vertical[j].copy())
                vertice.append(cycles_vertical[j])
            elif result[0] == 1:
                vertice.append(cycles_vertical[j])
                rectangle.append([result[1][0], min(cycles_vertical[j][1], cycles_vertical[j][2]), cycles_vertical[j][0], max(cycles_vertical[j][1], cycles_vertical[j][2])])
                current_edge.remove(result[1])
            elif result[0] == 2:
                
                vertical_line.append(cycles_vertical[j])
                #закрыли гешальт
                rectangle.append([result[1][0], min(result[1][1], result[1][2]), cycles_vertical[j][0] - (i + 1) / (2 * n + 3), max(result[1][1], result[1][2])])
                #добавили туясок
                rectangle.append([cycles_vertical[j][0] - (i + 1) / (2 * n + 3), max(result[1][1], result[1][2]), cycles_vertical[j][0] + (i + 1) / (2 * n + 3), min(result[1][1], result[1][2])])
                #закрыли маленьку штучку
                rectangle.append([cycles_vertical[j][0], min(cycles_vertical[j][1], cycles_vertical[j][2]), cycles_vertical[j][0] + (i + 1) / (2 * n + 3), max(cycles_vertical[j][1], cycles_vertical[j][2])])   
                #добавили два маленьких в кур эдж
                current_edge.append([cycles_vertical[j][0] + (i + 1) / (2 * n + 3), max(cycles_vertical[j][1], cycles_vertical[j][2]), max(result[1][1], result[1][2])])
                current_edge.append([cycles_vertical[j][0] + (i + 1) / (2 * n + 3), min(result[1][1], result[1][2]), min(cycles_vertical[j][1], cycles_vertical[j][2])])
                #удалили старье
                current_edge.remove(result[1])
            else:
                vertical_line.append(cycles_vertical[j])
                #завершили два прямоугольника
                rectangle.append([result[1][0], min(result[1][1], result[1][2]), cycles_vertical[j][0] - (i + 1) / (2 * n + 3), max(result[1][1], result[1][2])])
                rectangle.append([result[2][0], min(result[2][1], result[2][2]), cycles_vertical[j][0] - (i + 1) / (2 * n + 3), max(result[2][1], result[2][2])])
                #добавили маленький прямоугольник
                rectangle.append([cycles_vertical[j][0] - (i + 1) / (2 * n + 3), min(cycles_vertical[j][1], cycles_vertical[j][2]), cycles_vertical[j][0], max(cycles_vertical[j][1], cycles_vertical[j][2])])
                #добавили длинный 
                rectangle.append([cycles_vertical[j][0] - (i + 1) / (2 * n + 3), max(result[2][1], result[2][2]), cycles_vertical[j][0] + (i + 1) / (2 * n + 3), min(result[1][1], result[1][2])])

                current_edge.append([cycles_vertical[j][0] + (i + 1) / (2 * n + 3), min(result[1][1], result[1][2]), max(result[2][1], result[2][2])])

                current_edge.remove(result[2])
                current_edge.remove(result[1])
        k = 0
        while k < i:
            #Выше мы просто закрасили прямоугольник. теперь будем устронять плохие пересечения
            if incendent[cycles_copy.index(cycles[k])][cycles_copy.index(cycles[i])] != 0:
                for m in vertical_lines[k] + vertices[k]:
                    to_delete = []
                    for l in rectangle:
                        if l[1] > l[3]:
                            continue
                        if m[0] > l[0] and m[0] < l[2] and min(m[1], m[2]) > l[1] and max(m[1], m[2]) < l[3]:
                            rectangle.append([l[0], l[1], m[0] - (i + 1) / (2 * n + 3), l[3]])
                            rectangle.append([m[0] + (i + 1) / (2 * n + 3), l[1], l[2], l[3]])
                            rectangle.append([m[0] - (i + 1) / (2 * n + 3), l[3] , m[0] + (i + 1) / (2 * n + 3) , l[1]])
                            to_delete.append(l)
                    for l in to_delete:
                        rectangle.remove(l)
            k += 1
        vertical_lines.append(vertical_line)
        vertices.append(vertice)
        rectangles.append(rectangle)
        #осталось добавить вырезку старых кусков и вершин

print(rectangles)        