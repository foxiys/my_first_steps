import math
import random
 
print(math.pi**2, math.sqrt(9))
print(random.random(), random.choice([1, 2, 3, 4, 5]), '\n')
# print(len(str(2 ** 1000000)))
 
S = 'Port'
print(S, len(S), S[0], S[1], S[2], S[3])
print(S, len(S), S[-1], S[-2], S[-3], S[-4])
print(S, len(S), S[len(S)-1], S[len(S)-2], S[len(S)-3], S[len(S)-4])
print(S, len(S), S[1:], S[1:3], S[0:3], S[:3], S[:-1], S[:])
print(S, S+'xyz', S*8, S+S[0],'\n')
 
# S[0]=Z # так нельзя
S='Z'+S[1:]
print(S, S.find('r'), S.find('or'), S.replace('t','g'), '\n')
 
line='aaa,bbb,ccc,ddd'
L=line.split(',')
print(L[0], L[0].upper(), '\n')
 
print('{0} and {1}'.format('spam', 'SPAM!'), 'spam and SPAM!', '\n')
# список всех доступных атрибутов заданного объекта т.е. какие действия можно с этим объектом проводить
print(dir(S))
print(dir(L))
print(dir(-1), '\n')
# вызов справки о строковых методах
print(help(S.format),'\n')
