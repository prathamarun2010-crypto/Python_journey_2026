dict={
    "pratham": 1,
    "udtree": 2,
    "rohan": 3,
    "shivam": 4
}                             #dictionaries are mutable, unordered collections of key-value pairs. Each key is unique and maps to a value.
print(dict, type(dict))     
print(dict["pratham"])      #accessing value using key
dict["pratham"]=5          #updating value of key "pratham" to 5
print(dict)
dict.items()                 #returns a view object that displays a list of dictionary's key-value tuple pairs
print(dict.items())
dict.keys()                  #returns a view object that displays a list of dictionary's keys
print(dict.keys())
dict.values()                #returns a view object that displays a list of dictionary's values     
print(dict.values())
dict.pop("rohan")            #removes the key "rohan" and its corresponding value from the dictionary
print(dict) 
dict.get("udtree")             #returns the value associated with the key "udtree", or None if the key is not found
print(dict.get("udtree"))
dict.clear()                 #removes all key-value pairs from the dictionary, leaving it empty
print(dict)