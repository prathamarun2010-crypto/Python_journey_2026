#tuples are immutable lists.
friends=("udtree", 73, False, 3.14)
print(friends[0])
#friends[0]="xtral"         #unlike strings, tuples are immutable, meaning we cannot change their elements.
print(friends)
friends.count("udtree")     #returns the number of times "udtree" appears in the tuple
print(friends.count("udtree"))
friends.index("udtree")     #returns the index of the first occurrence of "udtree" in the tuple
print(friends.index("udtree"))
print(len(friends))           #returns the number of elements in the tuple
