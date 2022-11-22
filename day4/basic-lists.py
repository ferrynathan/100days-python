# https://docs.python.org/fr/3/tutorial/datastructures.html
america_states = ["delaware", "new jersey", "masachussets", "new york"]
print("the first state is " + america_states[0])
print("the third state is " + america_states[2])
print("the last state is " + america_states[-1])

america_states[2] = "prout"

america_states.append("new prout")
america_states.extend(["Nathan Land", "Caroline Land"])
print(america_states)
