# This is the parent class.
class Organism:

    # This is the parent class's method.
    # The child classes will override this method.
    def information(self):

        # This message is the default behavior of the parent class.
        return "This is an organism."


# This is the first child class.
# (Organism) means Human inherits from the Organism class.
class Human(Organism):

    # The Human class has its own first attribute.
    name = "MacGuyver"

    # The Human class has its own second attribute.
    occupation = "Engineer"

    # This method has the same name as the parent's method.
    # This is polymorphism because Human changes how information() works.
    def information(self):

# Return information specific to a Human.
return "My name is " + self.name + " and I am an " + self.occupation + "."


# This is the second child class.
# Dog also inherits from the Organism class.
class Dog(Organism):

    # The Dog class has its own first attribute.
    name = "Spot"

    # The Dog class has its own second attribute.
    breed = "Golden Retriever"

    # This method overrides the parent's information() method.
    # This is also polymorphism.
    def information(self):

        # Return information specific to a Dog.
        return "My name is " + self.name + " and I am a " + self.breed + "."


# This checks whether this file is being run directly.
if __name__ == "__main__":

    # Create an object from the Human class.
    human = Human()

    # Create an object from the Dog class.
    dog = Dog()

    # Call the information() method on the Human object.
    # Python uses Human's version of the method.
    print(human.information())

    # Call the information() method on the Dog object.
    # Python uses Dog's version of the method.
    print(dog.information())
