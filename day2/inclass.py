#!/usr/bin/env python3
a = [1,2,3,4]
b = a
a.append(5)
print(b)

a = [2,3,1]
a.sort()
print(a[0])
a.append(4)

a.pop()
print(a)

b = {"first":1, "second":2, "third":3}
b['first'] #will print the first value
b["fourth"]= 4
b.get("second", 0) #gives us 2, or 0 if key doesn't exist
del b['second'] #deletes this entry

c = set([1,2,3,4,4,4,4,5,5,5,5,5,5,5,5,6,6,7,8,9]) #deltes all repeted data an return only one of the duplication
print(c)

result = []
for i in range(10):
    result.append(i)

result = [i for i in range(10)]

result[:3]
result[3:]
result[2::3]
result[::-1]

for a in [1,2,3,4]:
    pass

for a in range(len([1,2,3,4,5])):
    pass

def add_one(x):
    return x + 1

answer = list(map(add_one, result))