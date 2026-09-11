
class Organism
    def information(self):
        return "This is an organism."



class Human(Organism):
    name = "MacGuyver"
    occupation = "Engineer"
    def information(self):
        return "My name is " + self.name + " and I am an " + self.occupation + "."


class Dog(Organism):
    name = "Spot".
    breed = "Golden Retriever"
    def information(self):
        return "My name is " + self.name + " and I am a " + self.breed + "."


if __name__ == "__main__":
    human = Human()
    dog = Dog()
    print(human.information())

    # Call the information() method on the Dog object.
    # Python uses Dog's version of the method.
    print(dog.information())
