# Parent class
class Animal:
    def __init__(self, name):
        self.name = name


# Child class 1
class Dog(Animal):
    def __init__(self, name, color, age):
        super().__init__(name)

        # Two attributes that belong to Dog
        self.color = color
        self.age = age


# Child class 2
class Cat(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name)

        # Two attributes that belong to Cat
        self.color = color
        self.breed = breed


# Create a dog
my_dog = Dog("Buddy", "Brown", 3)

# Print the dog's information
print(my_dog.name)
print(my_dog.color)
print(my_dog.age)


# Create a cat
my_cat = Cat("Luna", "White", "Persian")

# Print the cat's information
print(my_cat.name)
print(my_cat.color)
print(my_cat.breed)
