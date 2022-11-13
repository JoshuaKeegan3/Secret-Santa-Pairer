# Secret Santa Pairer

# Pairs people (strings) from a pool
# People can not be paired with themselves

# Imports
from random import shuffle

# Define randomised partisipants
pool = ["Joel", "Jack", "Addison", "Peoploe", "Phil", "Quinn", "Rex", "Ashan", "Max"]
shuffle(pool)

# Copy the partisipants and rotate the array
pool2 = pool.copy()
pool2.append(pool2.pop(0))

# Ouput
print(*zip(pool,pool2))
