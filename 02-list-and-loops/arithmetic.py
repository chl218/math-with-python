def average(a, b):
   return (a + b) / 2

a = True
b = 2
c = 0.5

type(a)
type(b)
type(c)

name_list = ['abe', 'bob', 'chloe', 'daphine']
score_list = [55, 63, 72, 54]

for i in range(4):
   print(name_list[i], score_list[i])

for i, name in enumerate(name_list):
   print(name, "has index", i)


def mySum(num):
   val = 0
   for i in range(num):
      val += 1
   return val

def average(numList):
   return sum(numList)/len(numList)

