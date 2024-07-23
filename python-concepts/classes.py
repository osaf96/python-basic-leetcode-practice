## CLASS 
# Classes are used to create new user-defined data structures that contain arbitrary information about something. For example:
class Dog:
    def __init__(self, breed):
        self.breed = breed
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
print(sam.breed)
print(frank.breed)
# The above code will print "Lab" and "Huskie" respectively

# You can also use class object attributes. For example:
class Dog:
    species = 'mammal'
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
sam = Dog('Lab', 'Sam')
print(sam.species)
# The above code will print "mammal"

# You can also use class methods. For example:
class Circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi
    def set_radius(self, radius):
        self.radius = radius
my_circle = Circle(3)
my_circle.set_radius(999)
print(my_circle.area())
# The above code will print 3108418.86

