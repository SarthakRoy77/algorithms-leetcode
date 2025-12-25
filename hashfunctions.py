#Hash table is a table of key:value pairs that is stored in an array forms of buckets or slots.
#A hash function is a function that converts the input and stores it in the hash table.
#For example, if we have a string "greg" , while g=7, r=18, e=5 the sum will be 37 
#Then we will mod it by the no.of buckets i.e. 37 % 5 = 2
#So the string "greg" will be stored in the index 2 of the hash table.
#When two keys hash to the same index, it is called a collision, in these case we use seperate chaining
#We can think as the seperate chaining as a linked list at each index of the hash table.
#One more way is linear probing, in this we find the next available slot in the hash table.
#But it is not efficient as it may lead to clustering of keys.
#There is one more thing which is hashmaps, it is just a pair of key:value pairs.Which in python is called dictionary. 


#Lets create a set , in python there is no need to create a set using hash functions as it is inbuilt.
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.add(5)
set1.add(6)

#Looking up a value in the set
if 3 in set1:
    print(True) 
else:
    print(False)

#Removing a value from the set
set1.remove(3)
#If the value is not present it will raise a KeyError to avoid this we can use discard method or use defaaltdict from collections module.
set1.discard(10) #This will not raise an error if 10 is not present
from collections import defaultdict
default_dict = defaultdict(int)
default_dict[1]

#Now lets create a hashmap using dictionary
hashmap = {"john":1112223333, "jane":4445556666, "doe":7778889999}
#Addding a new key:value pair
hashmap["alice"] = 1234567890
#Looking up a value using key
print(hashmap["jane"])
#Removing a key:value pair
del hashmap["doe"]
#If the key is not present it will raise a KeyError to avoid this we can use
value = hashmap.get("doe", "Not Found") #This will return "Not Found" if "doe" is not present
