alien_0 = {'color': 'green', 'points': 5}

# Accessing values in a dictionary
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You earned {new_points} points!')

# Adding new key-value pair
alien_0['x_coord'] = 0
alien_0['y_coord'] = 25

print(alien_0)