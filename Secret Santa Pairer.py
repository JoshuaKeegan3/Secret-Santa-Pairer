# Secret Santa Pairer

# Pairs people (strings) from a pool
# People can not be paired with themselves

# Imports
from random import shuffle

# Define randomised participants
pool = []
shuffle(pool)

# Copy the participants and rotate the array
pool2 = pool.copy()
pool2.append(pool2.pop(0))

# Ouput
print(*zip(pool,pool2))
