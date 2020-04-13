

'''
#Task1
list1 = []
b = [5,6,7,8,9]

c = b
+ list1
print(c)
d = [8,9,1,5,6,7,8]
c = c + d
print(c)
print(c.count(8))
print(sum(c)/len(c))
print(sum(c)+min(c)+max(c))

print("mean:",sum(c)/len(c))
print("median:",c[len(c)//2])

print(tuple(set(c)))


#Task2

set1 = {}
set2 = {}

#set1.update({7,8,9,1,2,3,4,5,0})  #we cant update empty list
#print(set1)

set1 = set()
set2 = set()
print(type(set1))
set1.update({7,8,9,1,2,3,4,5,0})
print(set1)
set2.update({4,5,6,0})
print(set2)

b = set2.issubset(set1)
print(b)

print(set1,set2)
c = set2.isdisjoint(set1)

print(c)

set1.remove(8)
print(set1)
set2.discard(0)
print(set2)

d = set1.union(set2)
print(sum(d))


# Task3
tuple1 = (1,4,5,6,7)
tuple2 = (5,6,7,8,9)


tuple1 = tuple(set(tuple1))
tuple2 = tuple(set(tuple2))

a = tuple1 + tuple2
print(a)
print(a.index(9))
set1 = {0,4,5}
print(type(a))
a = set(a)
print(type(a))
b = a.intersection(set1)
print(b)
a = tuple(a)
print(type(a))
print(a *3)
'''

#Task4:
a1 = {1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
print(a1[1][-1][1][4:])
print(a1[1][0:3])
k = a1[1][0:3]
print(tuple(k))
print(len(k))





