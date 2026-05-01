set_1={1,3,5,7,9}            #sets are mutable, unordered collections of unique elements. They are defined using curly braces {}.
set_2={2,4,6,8,10}
print(set, type(set))
set_1.add(11)                 #adds 11 to the set
print(set)
print(set_1.union(set_2))          #returns a new set that contains all the elements from both sets
print(set_1.intersection(set_2))   #returns a new set that contains only the elements that are present in both sets
print(set_1.difference(set_2))     #returns a new set that contains the elements that are present in set_1 but not in set_2


#sets are hashable, which means that they can be used as keys in a dictionary or as elements of another set. 
# However, since sets are mutable, they cannot be used as keys in a dictionary or as elements of another set.    