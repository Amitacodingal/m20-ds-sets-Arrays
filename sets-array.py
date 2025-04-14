# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set,"\n")

#remove a number from a set
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("After removing the first element from the said set:")
print(num_set,"\n")



#act2

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

#act 3
import array as arr

# create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))

# count number of occurences
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

# reverse the array 
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))

#acti4
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])

#use isdisjoint(). Return True if the set has no elements in common with other. 
print(x.isdisjoint(y))

#use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))

#new set with elements from both x and y
print(x | y)

#acp

def show_symmetric_difference(set1, set2):
    sym_diff = set1.symmetric_difference(set2)
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Symmetric Difference: {sym_diff}\n")

# A. Example with strings
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}
show_symmetric_difference(set1_a, set2_a)

# B. Example with integers
set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}
show_symmetric_difference(set1_b, set2_b)


