#Create 2 sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#Print all the items in set1
for x in set1:
    print(x)

#Find the unions of the sets
unions1 = set1.union(set2)
unions2 = set1 | set2
print("The unions are: ", unions1)
print("The unions are: ", unions2)

#Find the intersections of the sets
print("The intersections are: ", set1.intersection(set2))
print("The intersections are: ", set1 & set2)

#Find the differences of each set
print("The differences are: ", set1.difference(set2))
print("The differences are: ", set1 - set2)

#Add and remove elements from sets
set1.add(6)
set2.remove(8)
print(set1)
print(set2)
