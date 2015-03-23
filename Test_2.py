import re
 
# работа по шаблону
m=re.match('Hello[. \t]*(.*)world', 'Hello      .. Python ...     world')
print(m.group(1))
print(m)
help(m.group), '\n'
m1 = re.match('/(.*)/(.*)/(.*)', '/usr/home/www')
print(m1.group(0), m1.group(1), m1.group(2), m1.group(3), '\n')
 
# Списки
L=[123, 'port', 1.56464]
print(len(L), '\n', L[0], '\n', L[:-1], '\n', L+[4, 5, 6], '\n', L), '\n'
L.append('EXIT0')
print(L, '\n')
 
M=['aaa', 'ccc', 'bbb', 'fff', 'ddd', 'eee']
M.sort()
print(M)
M.reverse()
print(M, '\n')
 
# Вложенные списки(Матрицы)
M=[[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(M, '\n', M[1], '\n',  M[1][2])
