#Hash table is a table of key:value pairs that is stored in an array forms of buckets or slots.
#A hash function is a function that converts the input and stores it in the hash table.
#For example, if we have a string "greg" , while g=7, r=18, e=5 the sum will be 37 
#Then we will mod it by the no.of buckets i.e. 37 % 5 = 2
#So the string "greg" will be stored in the index 2 of the hash table.
#When two keys hash to the same index, it is called a collision, in these case we use seperate chaining
#We can think as the seperate chaining as a linked list at each index of the hash table.