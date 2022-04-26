#Tuples are used to store multiple items in a single variable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)


thistuple = ("apple1", "banana1", "cherry1")
print(len(thistuple))


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

