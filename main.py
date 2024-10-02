import math
class1 = int(input("Введите количество учащихся в первом классе: "))
class2 = int(input("Введите количество учащихся во втором классе: "))
class3 = int(input("Введите количество учащихся в третьем классе: "))
people = class1 + class2 + class3
desks1 = math.ceil(class1/ 2)
desks2 = math.ceil(class2 / 2)
desks3 = math.ceil(class3 / 2)
desks =  desks1 + desks2 + desks3
print("Необходимо закупить парт:", desks)
