import numpy as np

# Проверка в строке, столбце и субматрице
def isCheck(m, a, b, num):
    n = 3 * (int(a / 3)) + int(b / 3)
    x = 3 * int(n / 3)
    y = 3 * (n - x)
    return num in m[x:x + 3, y:y + 3] or num in m[0:9, b] or num in m[a, 0:9]

def ListRemove(list, num, n):
    if num in list[n]:
        list[n].remove(num)

def length(l):
    t = 0
    for i in range(9):
        t += len(l[i])
    return t

# решальшик для простых
def Solver(m,list):
    check = 0
    l = length(list)
    while l != check:
        l = length(list)
        for x in range(0, 9):
            for y in range(0, 9):
                if m[x, y] == 0:
                    n = 3 * (int(x / 3)) + int(y / 3)
                    ch = 0
                    for i in range(len(list[n])):
                        if not isCheck(m, x, y, list[n][i]):
                            ch += 1
                            if ch > 1:
                                break
                            temp = i
                    if ch == 1:
                        m[x, y] = list[n][temp]
                        del list[n][temp]
        check = length(list)

def Search(m):
    for x in range(0, 9):
        for y in range(0, 9):
            if m[x, y] == 0:
                return True, x, y
    return False, x, y

# решальшик для сложных
def Attempt(m, list):
    m_temp = np.copy(m)
    test, x, y = Search(m)
    if test:
        n = 3 * (int(x / 3)) + int(y / 3)
        ch = False
        for i in range(len(list[n])):
            if not isCheck(m, x, y, list[n][i]):
                ch = True
                m[x, y] = list[n][i]
            if ch is True:
                check, m = Attempt(m, list)
                if check is True:
                    return True, m
                elif check is False:
                    m = np.copy(m_temp)
                    ch = False
        if ch is False:
            return False, m
    else:
        return True, m

# Комбинация Простого и сложного решальщика
def Solve(m, list):
    Solver(m,list)
    check, m = Attempt(m, list)
    return m

# m = np.matrix([
# [6,4,0, 0,1,3, 0,7,0],
# [3,0,0, 6,0,8, 0,1,5],
# [8,1,2, 5,7,0, 0,3,0],
# [2,0,0, 4,0,5, 1,0,7],
# [4,0,7, 0,0,0, 9,0,3],
# [0,8,0, 7,9,6, 5,0,2],
# [0,2,0, 3,0,7, 6,5,0],
# [7,0,8, 1,5,0, 3,9,0],
# [0,3,1, 0,6,4, 0,0,8]])
#
# m = np.matrix([
# [0,0,0, 5,0,7, 0,0,0],
# [0,0,2, 4,0,6, 3,0,0],
# [0,9,0, 0,1,0, 0,2,0],
# [2,7,0, 0,0,0, 0,6,8],
# [0,0,3, 0,0,0, 1,0,0],
# [1,4,0, 0,0,0, 0,9,3],
# [0,6,0, 0,4,0, 0,5,0],
# [0,0,9, 2,0,5, 6,0,0],
# [0,0,0, 9,0,3, 0,0,0]])
#
m = np.matrix([
[4,0,0, 8,0,0, 0,0,0],
[0,0,7, 0,6,0, 0,0,5],
[0,0,3, 0,0,0, 0,9,0],
[0,0,4, 0,0,1, 0,0,7],
[0,5,0, 0,0,8, 0,1,0],
[2,0,0, 0,0,0, 3,0,0],
[0,2,0, 0,0,0, 4,0,0],
[9,0,0, 0,3,0, 6,0,0],
[0,0,0, 0,0,7, 0,0,3]])


# создание листов с не использованными цифрами для каждой субматрицы
list = [[i for i in range(1, 10)]]
for i in range(8):
    list.append([i for i in range(1, 10)])

for x in range(0, 9):
      for y in range(0, 9):
          n = 3 * (int(x / 3)) + int(y / 3)
          ListRemove(list, m[x, y], n)
#
print(m)
m = Solve(m, list)

# Check, m = Attempt(m, list)
print(m)

