## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Aminal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish has-a object
class Fish(object):

    def __init__(self, name):
        self.name = name

## Salmon ia-a Fish
class Salmon(Fish):

    def __init__(self, name):
        self.name = name

## Halibut is-a Fish
class Halibut(Fish):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "%s is a Halibut and is %d years old" % (name, age)


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## fran has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish("Flipper")

## crouse is-a Salmon
crouse = Salmon("Crouse")

## harry is-a Halibut
harry = Halibut("Harry", 4)
