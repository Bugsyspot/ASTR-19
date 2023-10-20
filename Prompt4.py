
x = 10
y = 5

class Animal:
    def __init__(self, arm_length="3 feet", leg_length="1.3 feet", num_eyes="2", has_tail="true", is_furry="false"):
        self.length = arm_length
        self.length = leg_length
        self.eyes = num_eyes

    def describe(self):
        print("Physical Description of a Turtle:")
        print(f"A turtle's flippers are about {self.length} long")
        print(f"A turtle's hind flippers are about {self.length} long")
        print(f"A turtle has {self.eyes} eyes")
        print(f"A turtle has a tail:{bool(x < y)} ")
        print(f"A turtle is furry:{bool(x == y)} ")

A = Animal('Turtle')
print(A.describe())