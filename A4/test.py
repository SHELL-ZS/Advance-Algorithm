import random
i = range(6)
'''for n in i:
  print(n)'''
j = range(1,7)
'''for n in j:
  print(n)'''


x = [[1,2],[1,3]]
x = [1.0] * 4
cost = []
for e in range(10):
  cost.append(random.uniform(-1,1))

weights = [1.0]*10
outcome = [bool(random.getrandbits(1)) for i in range(100)]
expert_three = []
accuracy = 0.6
for o in outcome:
  population = [o,not o]
  weight = [accuracy, 1-accuracy]
  expert_three = expert_three + random.choices(population,weight)

count = 0
for i in range(len(outcome)):
  if outcome[i] == expert_three[i]:
    count += 1

a = count/len(outcome)

expert_four = []
expert_four.append(bool(random.getrandbits(1)))
d = 1
while d <= 10:
  next = not expert_four[d-1]
  expert_four.append(next)
  d += 1

weights = [1,2,3,41,3,5,5]
max_weight = weights.index((max(weights)))
print(expert_four)