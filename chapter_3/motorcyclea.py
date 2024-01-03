def lineBreak():
    print("----------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
lineBreak()

# Change the first element 
motorcycles[0] = 'ducati'
print(motorcycles)
lineBreak()

# Adding Elementto a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # adds element to the last position of the list
lineBreak()

# Insert element at a certain position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
lineBreak()

# Remove element from the list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0] # If we know the position then we can use the 'del' keyword
print(motorcycles)
lineBreak()

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()

