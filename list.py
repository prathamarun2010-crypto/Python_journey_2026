friends=["udtree", 73, False, 3.14]
print(friends[0])
friends[0]="xtral"         #unlike strings, lists are mutable, meaning we can change their elements.
print(friends)
friends.insert(2, "udtree")   #inserts "udtree" at index 2, shifting the rest of the elements to the right
print(friends)
friends.append("gengar")     #adds "gengar" to the end of the list
print(friends)
friends.append("gengar")     #adds "gengar" to the end of the list
print(friends)
friends.remove("gengar")     #removes the first occurrence of "gengar" from the list
print(friends)