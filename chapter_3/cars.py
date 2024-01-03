cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # changes the order of the list permanently i.e., can't revert to original order
print(cars)

# Reverse-alphabetical sorting
cars.sort(reverse = True) # changes the order of the list permanently i.e., can't revert to original order
print(cars)

# There is a way to sort the list temporarily. With help of sorted() fuction.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original List:")
print(cars)

print("\nSorted List")
print(sorted(cars))

print("\nOriginal List again:")
print(cars)
print("--------------------------------------")

# Print list in reverse order. reverse() changes the order of list permanently.
# We can revert back to original list again by applyling reverse() again on same list second time.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print("--------------------------------------")

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
