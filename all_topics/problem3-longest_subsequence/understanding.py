# Step 1: Define the class
class StringManipulator:
    # Constructor to initialize the class
    def __init__(self, str1, str2):
        self.str1 = str1  # First string
        self.str2 = str2  # Second string

    # Step 2: Add a method to concatenate the strings
    def concatenate(self):
        return self.str1 + "##" + self.str2

# Step 3: Create objects of the class
# Object 1
obj1 = StringManipulator("Hello", "World")
print("Object 1 concatenation result:", obj1.concatenate())  # Output: Hello World

# Object 2
obj2 = StringManipulator("Python", "Programming")
print("Object 2 concatenation result:", obj2.concatenate())  # Output: Python Programming