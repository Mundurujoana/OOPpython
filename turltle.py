class Bird:
    def __init__(self, weight):
        self.__weight = weight

    def weight(self):
        return self.__weight

    def __repr__(self):
        return "Bird, weight = " + str(self.__weight)

# Create a list of Bird objects.
birds = []
birds.append(Bird(10))
birds.append(Bird(5))
birds.append(Bird(200))

# Sort the birds by their weights.
birds.sort(key = len)

# Display sorted birds.
for b in birds:
    print(b)