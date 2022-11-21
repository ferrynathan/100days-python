import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_full = random.random()*5  # random float between 0 and 5 not included)
print(random_full)

print(my_module.pi)
