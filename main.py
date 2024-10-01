import math
class1 = int(input("Введите количество учащихся в первом классе: "))
class2 = int(input("Введите количество учащихся во втором классе: "))
class3 = int(input("Введите количество учащихся в третьем классе: "))
people = class1 + class2 + class3
desks = math.ceil(people / 2)
print("Необходимо закупить парт:", desks)
