#Testing out the module of the week, starting with the random module.

import random

for i in range(10):
    print('\n%04.3f' % random.random(), end=' ')
print()

for i in range(5):
    print('\n{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()

random.seed(1)

for i in range(10):
    print('\n{:04.3f}'.format(random.random()), end=' ')
print()

import random
import os
import pickle

if os.path.exists('state.dat'):
    print("Loading state from file...")
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    print("No state.dat, seeding")
    random.seed(1)

for i in range(3):
    print('\n{:04.3f}'.format(random.random()), end=' ')
print()

with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

print("State saved to state.dat")
for i in range(3):
    print('\n{:04.3f}'.format(random.random()), end=' ')
print()