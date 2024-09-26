import random
from itertools import count

from random import randint
# 1 задача

print("1 задача")
tovar=tuple(random.randint(500,1500)for _ in range(12))
totalCOast=sum(c for c in tovar if c>=1000)
print("общаяя цена: ",totalCOast)
print("массив: ",tovar)

# 2 задача

print("2 задача")
def average(tovar):
    average = sum(tovar) / len(tovar)
    difference = [abs(x - average) for x in tovar]
    closest_index = difference.index(min(difference))
    return closest_index, tovar[closest_index]

coordinates = average(tovar)
av=sum(tovar) / len(tovar)
print("среднее",av)
print("индекс элемента :", coordinates[0])
print("значение элемента :", coordinates[1])

# 3 задача

print("3 задача")
numbers=[1,2,3,4,5,6,7,8,91,0,1,124,5,12346,25,727,364,7]
for number in numbers:
    if number%2==0:
        print(number, end=" ")
        continue
print(".")

# 4 задача

print("4 задача")
other = {4, 5, 6}
my={1,2,3}
union = my.union(other)
for i in union:
    if i % 1==i:
        print(i)###это заглушка ебать
print("кол-во э-в: ",i)

# 5 задача(че курили когда ее состовляли?)
print("5 задача")
synonyms = {
    'a': 'aa',
    'q': 'qq',
    'w': 'ww',
    'e': 'ee',
    'r': 'rr'
}
word='q'
if word in synonyms:
    print("синоним:",word)
else:
    found=next((k for k,v in synonyms.items()if v==word),None)
    if found:
        print("синоним найден:",found)
    else:
        print("синоним не найден")