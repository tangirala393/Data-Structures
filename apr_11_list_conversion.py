
'''

list1 = [1,2,3,4,5,"krishna","python"]

print(type(list1))

list2 = 1,2,3,4,"r"
print(type(list2))
list1 = tuple(list1)     #list to tuple conversion is fine
print(type(list1))
print(list2)

list2 = list(list2)      #Tuple to list conversion is fine
print(type(list2))


# count
a = (1,2,5,6,"k","r",5,6,5)


print(a.count(5))
print(a.clear())        #AttributeError: 'tuple' object has no attribute 'clear'       
print(a)
del(a)
print(a)

print(a.index(5))


# Conversion from list-->set,list-->set,set-->list,set-->tuple
# As o now All coversions is possible

list1 = [1,3,5,"pytho","welcome"]
set1 = {1,'f',4,56,"krishna"}
print(type(set1))
print(type(list1))
list1 = set(list1)

print(type(list1))
print(list1)
list1 = tuple(list1)
print(list1)
print(type(list1))

list1 = list(list1)
print(list1)
print(type(list1))

list1 = tuple(list1)
print(list1)
print(type(list1))

list1 = set(list1)
print(list1)
print(type(list1))


'''
a = [1,2,3,4,5,7,8,5,78,5]

print(a.count(5))

